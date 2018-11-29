from locate_source import dtr_algorithm
import argparse
from tqdm import tqdm


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--strategy_of_observer", help="how to select observers")
parser.add_argument("-r", "--rate_of_infection", help="the infection of propagation, 5 or 10")
args = parser.parse_args()


def observers_proportion(beta, network_type, network_size, observers_strategy,
                         ba_m=3, er_m=0, num_iteration=100, candidate=False):
    """
    test the dtr_algorithm in different setting of observers proportion across different rate of infection 
    :return: 
    """
    hit_rate_across_rate_obs = []
    get_rate_across_rate_obs = []
    for rate_obs in tqdm(range(0, 100, 2)):
        hit_rate = 0.0
        get_rate = 0.0
        for i in range(num_iteration):
            locate_rank, source_node = \
                dtr_algorithm(network_type, network_size, observers_strategy, rate_obs/100, er_m, ba_m,
                              beta=beta, candidate=candidate)
            if len(locate_rank) != 0 and locate_rank[0] == source_node:
                hit_rate += 1
            if source_node in locate_rank[:int(network_size*0.1)]:
                get_rate += 1
        hit_rate /= num_iteration
        get_rate /= num_iteration
        hit_rate_across_rate_obs.append(hit_rate)
        get_rate_across_rate_obs.append(get_rate)

    file_name = "../plot/observer_strategy/"+str(network_type)+str(network_size)+\
                observers_strategy+str(candidate)+str(beta)+".txt"
    with open(file_name, "w") as f_out:
        for h, g in zip(hit_rate_across_rate_obs, get_rate_across_rate_obs):
            f_out.write(str(h) + "\t" + str(g) + "\n")


def across_diff_beta(network_type, network_size, observers_strategy, er_m, ba_m, num_iteration, candidate):
    start = int(args.rate_of_infection)
    for rate_of_infection in range(start, start+1):
        print("beta = " + str(rate_of_infection/10))
        observers_proportion(rate_of_infection/10, network_type, network_size,
                             observers_strategy, ba_m, er_m, num_iteration, candidate)

if __name__ == "__main__":
    ba_parameters = {
        "network_type": "ba",
        # "network_type": "er",
        "network_size": 100,
        "observers_strategy": args.strategy_of_observer,
        "er_m": 300,
        "ba_m": 3,
        "num_iteration": 10000,
        "candidate": True
    }

    across_diff_beta(
        ba_parameters["network_type"],
        ba_parameters["network_size"],
        ba_parameters["observers_strategy"],
        ba_parameters["er_m"],
        ba_parameters["ba_m"],
        ba_parameters["num_iteration"],
        ba_parameters["candidate"]
    )
