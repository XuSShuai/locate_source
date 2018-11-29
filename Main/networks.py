import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt


def generate_graph(network_type, network_size, er_m=0, ba_m=3, er_sy_p=0.1, print_info=False):
    """
    :param network_type: string type, "ba", "er_sy" or "er"
    :param network_size: int scalar, node size in the network
    :param er_m: int scalar, specify the size of edges, generate the ER graph use function defined by self
    :param ba_m: int scalar, number of edges to attach from a new node to existing nodes during BA generate
    :param er_sy_p: float scalar, specify the size of edges, generate the ER graph use the build-in function of networkx
    :param print_info: whether or not the show the information about network
    :return: 
    """
    net = nx.Graph()
    if network_type == "ba":
        net = nx.random_graphs.barabasi_albert_graph(n=network_size, m=ba_m)
    elif network_type == "er":
        net = er_graph(network_size, er_m)
    elif network_type == "er_sy":
        net = nx.random_graphs.erdos_renyi_graph(n=network_size, p=er_sy_p)
    else:
        print("network type error!")
        exit()

    if print_info:
        print("details about network:")
        print(nx.info(net))
        all_degree = np.array(nx.degree(net))
        print("Average degree: ", np.mean([x[1] for x in all_degree]))
        print("Max degree: ", np.max([x[1] for x in all_degree]))
        print("Min degree: ", np.min([x[1] for x in all_degree]))
        print()
        if network_type == "ba":
            pos = nx.spring_layout(net)
        elif network_type == "er":
            pos = nx.shell_layout(net)
        nx.draw(net, pos, with_labels=True, node_size=np.array([x[1] for x in all_degree])*10)
        plt.savefig("./MAIN_debug_output/" + network_type + str(network_size) + "network.jpg")

    return net


def er_graph(network_size, er_m):
    """
    :param network_size: nodes in the network 
    :param er_m: edges in the network
    :return: graph
    """
    er = nx.Graph()

    complete_graph = nx.random_graphs.complete_graph(network_size, nx.Graph())
    er_edges = random.sample(complete_graph.edges(), er_m)

    er.add_nodes_from([x for x in range(network_size)])
    er.add_edges_from(er_edges)

    return er


if __name__ == "__main__":
    pass
    # debug
    # ba = generate_graph(network_type="ba", network_size=50, ba_m=3, print_info=True)
    # print("-" * 20)
    # er = generate_graph(network_type="er", network_size=50, er_m=500, print_info=True)
