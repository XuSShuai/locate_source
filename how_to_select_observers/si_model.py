import numpy as np
import networkx as nx
from networks import generate_graph


def si_diffusion(beta, network_type, network_size, er_m=0, ba_m=3, debug=False):
    """
    :param beta: float, rate of infection 
    :param network_type: string, "er" or "ba"
    :param network_size: int, number of nodes
    :param er_m: int scalar, specify the size of edges, generate the ER graph use function defined by self
    :param ba_m: int scalar, number of edges to attach from a new node to existing nodes during BA generate
    :param debug:
    :return: log of propagating
    """

    while True:
        network = generate_graph(network_type, network_size, er_m, ba_m, print_info=debug)
        if nx.is_connected(network):
            break
    if debug:
        print("network generated!")

    network_dict = dict()
    for i in range(network_size):
        network_dict[i] = []
    for edges in network.edges():
        network_dict[edges[0]].append(edges[1])
        network_dict[edges[1]].append(edges[0])
    # for key, value in network_dict.items():
    #     print(key, ":", value)
    # print("number of nodes: ", len(network_dict.keys()))
    # print("number of edges: ", np.sum([len(x) for x in network_dict.values()]))

    nodes_infected_or_not = np.zeros_like([x for x in network_dict.keys()])
    nodes_infected_from_who = np.zeros_like([x for x in network_dict.keys()])
    nodes_infected_time = np.zeros_like([x for x in network_dict.keys()])

    source_node = np.random.randint(0, network_size)
    if debug:
        print("Source Node is: ", source_node)
    nodes_infected_or_not[source_node] = 1
    nodes_infected_from_who[source_node] = 0
    nodes_infected_time[source_node] = 1
    clock = 1
    while True:
        clock += 1
        if debug: print(clock, "-" * 50)
        # if all the person has been infected, break
        if np.sum(nodes_infected_or_not) == network_size:
            if debug: print("propagate completed!")
            break
        # get all the persons who have already been infected
        nodes_have_been_infected = np.argwhere(np.array(nodes_infected_or_not) == 1).reshape(1, -1)[0]
        if debug: print("nodes_have_been_infected\n", nodes_have_been_infected)

        # random select the individual of infected and try to infect their neighbors
        # who have not infected yet with the rate of infection `beta`
        np.random.shuffle(nodes_have_been_infected)   # shuffle

        for infected_individual in nodes_have_been_infected:
            if debug: print("   infected_individual:", int(infected_individual))
            no_infected_neighbors = [x for x in network_dict[int(infected_individual)]
                                     if nodes_infected_or_not[x] == 0]
            if debug: print("      no_infected_neighbors:",no_infected_neighbors)
            for no_infected in no_infected_neighbors:
                pro = np.random.random()
                if pro < beta:
                    if debug: print("         info from %s -> %s" % (infected_individual, no_infected))
                    nodes_infected_or_not[no_infected] = 1
                    nodes_infected_from_who[no_infected] = infected_individual
                    nodes_infected_time[no_infected] = clock

    neighbors_of_source = list(nx.neighbors(network, source_node))
    nodes_infected_from_who[source_node] = neighbors_of_source[np.random.randint(0, len(neighbors_of_source))]
    if debug:
        print(nodes_infected_from_who)
        print(nodes_infected_time)
    return nodes_infected_time, nodes_infected_from_who, network, source_node

if __name__ == "__main__":
    pass
    # debug
    si_diffusion(0.5, "er", 10, er_m=10, debug=True)