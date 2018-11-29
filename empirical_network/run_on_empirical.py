from locate_source import dtr_algorithm
import numpy as np
import networkx as nx
import argparse
from tqdm import tqdm


parser = argparse.ArgumentParser()
parser.add_argument("-n", "--network_name", help="network name, {Celegans, florida, Metabolic, USAir}")
args = parser.parse_args()


def load_empirical(file_path, show=False):
    G = nx.Graph()
    data = np.loadtxt(file_path, dtype=np.int64)
    if min(min(data[:, 0]), min(data[:, 1])) == 1:
        G.add_edges_from(data - 1)
    else:
        G.add_edges_from(data)
    if show:
        print("load data from " + file_path)
        print("number of nodes: ", G.number_of_nodes())
        print("number of edges: ", G.number_of_edges())
        print("is full connected: ", not G.is_multigraph())

    return G


def observers_proportion(network, network_name, beta, observers_strategy, num_iteration=100, candidate=False):
    """
    test the dtr_algorithm in different setting of observers proportion across different rate of infection 
    :return: 
    """
    hit_rate_across_rate_obs = []
    get_rate_across_rate_obs = []
    network_size = network.number_of_nodes()
    for rate_obs in tqdm(range(0, 100, 2)):
        hit_rate = 0.0
        get_rate = 0.0
        for i in range(num_iteration):
            locate_rank, source_node = \
                dtr_algorithm(network, observers_strategy, rate_obs/100, beta=beta, candidate=candidate)
            if len(locate_rank) != 0 and locate_rank[0] == source_node:
                hit_rate += 1
            if source_node in locate_rank[:int(network_size*0.1)]:
                get_rate += 1
        hit_rate /= num_iteration
        get_rate /= num_iteration
        hit_rate_across_rate_obs.append(hit_rate)
        get_rate_across_rate_obs.append(get_rate)

    save_name = "../plot/empirical_network/" + args.network_name + "/"+str(network_name)+observers_strategy+str(candidate)+str(beta)+".txt"
    with open(save_name, "w") as f_out:
        for h, g in zip(hit_rate_across_rate_obs, get_rate_across_rate_obs):
            f_out.write(str(h) + "\t" + str(g) + "\n")


def across_diff_beta(network, network_name, observers_strategy, num_iteration, candidate):
    for rate_of_infection in range(1, 11, 1):
        print("beta = " + str(rate_of_infection/10))
        observers_proportion(network, network_name, rate_of_infection/10, observers_strategy, num_iteration, candidate)

if __name__ == "__main__":
    file_name = "./network_data/" + args.network_name + ".data"

    network = load_empirical(file_name)

    parameters = {
        "observers_strategy": "max_degree",
        "num_iteration": 10000,
        "candidate": True
    }

    across_diff_beta(
        network,
        args.network_name,
        parameters["observers_strategy"],
        parameters["num_iteration"],
        parameters["candidate"]
    )
