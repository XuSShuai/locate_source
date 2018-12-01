import numpy as np
import networkx as nx
from si_model import si_diffusion
from scipy.stats import pearsonr


def select_observers(network, strategy, proportion=0.1, tread_off=0.1):
    """
    :param network: 
    :param strategy: 
        "max_degree":
        "min_degree":
        "max_k_shell":
        "min_k_shell":
        "max_betweenness":
        "min_betweenness":
        "max_closeness":
        "min_closeness":
        "random":
    :param proportion: percentage of observers
    :param tread_off: mix strategy of max_degree and min_degree
    :return: 
    """
    observer_nodes_size = int(nx.number_of_nodes(G=network) * proportion)
    observers = []
    if strategy == "max_degree":
        degree_dict = dict(nx.degree(network))
        degree_sorted_by_value = sorted(degree_dict.items(), key=lambda x: x[1], reverse=True)
        observers = [x[0] for x in degree_sorted_by_value][:observer_nodes_size]
    elif strategy == "min_degree":
        degree_dict = dict(nx.degree(network))
        degree_sorted_by_value = sorted(degree_dict.items(), key=lambda x: x[1])
        observers = [x[0] for x in degree_sorted_by_value][:observer_nodes_size]
    elif strategy == "max_k_shell":
        k_core_dict = dict(nx.core_number(G=network))
        k_core_sorted = sorted(k_core_dict.items(), key=lambda x: x[1], reverse=True)
        observers = [x[0] for x in k_core_sorted][:observer_nodes_size]
    elif strategy == "min_k_shell":
        k_core_dict = dict(nx.core_number(G=network))
        k_core_sorted = sorted(k_core_dict.items(), key=lambda x: x[1])
        observers = [x[0] for x in k_core_sorted][:observer_nodes_size]
    elif strategy == "max_betweenness":
        between_centrality = dict(nx.betweenness_centrality(G=network))
        between_centrality_stored = sorted(between_centrality.items(), key=lambda x: x[1], reverse=True)
        observers = [x[0] for x in between_centrality_stored][:observer_nodes_size]
    elif strategy == "min_betweenness":
        between_centrality = dict(nx.betweenness_centrality(G=network))
        between_centrality_stored = sorted(between_centrality.items(), key=lambda x: x[1])
        observers = [x[0] for x in between_centrality_stored][:observer_nodes_size]
    elif strategy == "max_closeness":
        closeness_centrality = dict(nx.closeness_centrality(G=network))
        closeness_centrality_stored = sorted(closeness_centrality.items(), key=lambda x: x[1], reverse=True)
        observers = [x[0] for x in closeness_centrality_stored][:observer_nodes_size]
    elif strategy == "min_closeness":
        closeness_centrality = dict(nx.closeness_centrality(G=network))
        closeness_centrality_stored = sorted(closeness_centrality.items(), key=lambda x: x[1])
        observers = [x[0] for x in closeness_centrality_stored][:observer_nodes_size]
    elif strategy == "random":
        observers = np.random.randint(0, nx.number_of_nodes(network), observer_nodes_size)

    return observers


def candidate_sources(network, observers, nodes_infected_from_who):
    un_observer_nodes = set(network.nodes())
    candidate_source_list = []
    for un_observer in un_observer_nodes:
        scores = 0
        for observer in observers:
            if nx.shortest_path_length(G=network, source=un_observer, target=observer) > \
                    nx.shortest_path_length(G=network, source=un_observer, target=nodes_infected_from_who[observer]):
                scores += 1
        if scores > int(0.5000 * len(observers)):
            candidate_source_list.append(un_observer)

    return candidate_source_list


def cos_similarity(sequence1, sequence2):
    return np.sum((np.array(sequence1) * np.array(sequence2)))/(np.linalg.norm(sequence1) * np.linalg.norm(sequence2))


def pearson_similarity(sequence1, sequence2):
    return pearsonr(sequence1, sequence2)[0]


def dtr_algorithm(network_type, network_size, observers_strategy, observers_rate=0.1,
                  er_m=0, ba_m=3, beta=0.9, candidate=False, print_detail_info=False):
    """
    :param network_type: 
    :param network_size: 
    :param observers_strategy: 
    :param observers_rate: 
    :param er_m: 
    :param ba_m: 
    :param beta: 
    :param candidate: 
    :param print_detail_info: 
    :return: 
    """
    if print_detail_info:
        print("network type: ", network_type)
        print("network size: ", network_size)
        print("how to determine the observers: ", observers_strategy)
        print("proportion of observers: ", observers_rate)
        print("rate of infection: ", beta)
        print("whether or not use candidate source node: ", candidate)
        print()

    scores = dict()
    # create network, and propagation on it.
    nodes_infected_time, nodes_infected_from_who, net, source_node = \
        si_diffusion(beta, network_type, network_size, er_m, ba_m, debug=False)
    observers = select_observers(net, observers_strategy, observers_rate)

    if candidate:
        candidate_sources_list = candidate_sources(net, observers, nodes_infected_from_who)
    else:
        candidate_sources_list = set(net.nodes())

    observers_infected_times = [nodes_infected_time[x] for x in observers]
    for node in candidate_sources_list:
        distance_2_observers = [nx.shortest_path_length(net, node, x) for x in observers]
        source_score = cos_similarity(observers_infected_times, distance_2_observers)
        # source_score = pearson_similarity(observers_infected_times, distance_2_observers)
        scores[node] = source_score

    scores_sorted = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    if print_detail_info:
        print("the true source is: ", source_node)
        # print("->".join([str(i) for i in np.argsort(nodes_infected_time)[:20]]))
        print("\nalgorithm output: ")
        for key, value in scores_sorted[:20]:
            print("\tnode: %d probability %6f to be source." % (key, value))
        print("\t...")
        print([x[0] for x in scores_sorted][0], "has the most probability node to be source!")

    return [x[0] for x in scores_sorted], source_node


if __name__ == "__main__":
    # debug
    dtr_algorithm("ba", 100, "max_degree", 0.1, ba_m=3, beta=0.9, candidate=False, print_detail_info=True)
    # or
    # dtr_algorithm("er", 100, "max_degree", 0.1, er_m=500, beta=0.9, candidate=False, print_detail_info=True)
