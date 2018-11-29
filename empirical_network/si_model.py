import numpy as np
import networkx as nx
from networks_empirical import load_empirical


def si_diffusion(network, beta, debug=False):
    """
    :param beta: float, rate of infection 
    :param print_info:
    :return: log of propagating
    """

    if not nx.is_connected(network):
        print("is not connected")
        exit()
    if debug:
        print("network generated!")

    network_dict = dict()
    for i in range(network.number_of_nodes()):
        network_dict[i] = []
    for edges in network.edges():
        network_dict[edges[0]].append(edges[1])
        network_dict[edges[1]].append(edges[0])

    nodes_infected_or_not = np.zeros_like([x for x in network_dict.keys()])
    nodes_infected_from_who = np.zeros_like([x for x in network_dict.keys()])
    nodes_infected_time = np.zeros_like([x for x in network_dict.keys()])

    source_node = np.random.randint(0, network.number_of_nodes())
    if debug:
        print("Source Node is: ", source_node)
    nodes_infected_or_not[source_node] = 1
    nodes_infected_from_who[source_node] = 0
    nodes_infected_time[source_node] = 1
    clock = 1
    while True:
        clock += 1
        # if all the person has been infected, break
        if np.sum(nodes_infected_or_not) == network.number_of_nodes():
            if debug:
                print("propagate completed!")
            break

        # get all the persons who have already been infected
        nodes_have_been_infected = np.argwhere(np.array(nodes_infected_or_not) == 1).reshape(1, -1)[0]

        # random select the individual of infected and try to infect their neighbors
        # who have not infected yet with the rate of infection `beta`
        np.random.shuffle(nodes_have_been_infected)   # shuffle

        for infected_individual in nodes_have_been_infected:
            no_infected_neighbors = [x for x in network_dict[int(infected_individual)]
                                     if nodes_infected_or_not[x] == 0]
            for no_infected in no_infected_neighbors:
                pro = np.random.random()
                if pro < beta:
                    nodes_infected_or_not[no_infected] = 1
                    nodes_infected_from_who[no_infected] = infected_individual
                    nodes_infected_time[no_infected] = clock

    neighbors_of_source = list(nx.neighbors(network, source_node))
    nodes_infected_from_who[source_node] = neighbors_of_source[np.random.randint(0, len(neighbors_of_source))]
    return nodes_infected_time, nodes_infected_from_who, network, source_node

if __name__ == "__main__":
    pass
    network = load_empirical("./network_data/USAir.data")
    si_diffusion(network, .5)