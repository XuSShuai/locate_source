import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (7, 5)

FOLDER_PATH = "./observer_strategy/"
strategy_list = [
    "max_betweenness",
    "max_degree",
    "max_k_shell",
    "min_betweenness",
    "min_degree",
    "min_k_shell",
    "random"
]
symbols = ['o', 'v', '*', 's', 'D', '^', 'H']
X_RANGE = [x/50 for x in range(50)]
COLORS = ['bisque','lightgreen','slategrey','lightcoral',
          'orchid','cornflowerblue','silver']


def plot(type, rate, hit_get, legend=False):
    for index, strategy in enumerate(strategy_list):
        file_name = FOLDER_PATH + type + "100" + strategy + "True" + rate + ".txt"
        data = np.loadtxt(file_name)
        if hit_get == "hitting rate":
            plt.plot(X_RANGE, data[:, 0], marker=symbols[index],
                     alpha = 0.718, color=COLORS[index], label=strategy, ms=6)
        if hit_get == "getting rate":
            plt.plot(X_RANGE, data[:, 1], marker=symbols[index],
                     alpha = 0.718, color=COLORS[index], label=strategy, ms=6)
    plt.xlabel("observers proportion", fontsize=13)
    plt.ylabel(hit_get, fontsize=14)
    plt.title("infection rate = " + rate, fontsize=16)
    if legend:
        plt.legend(shadow=True)
    plt.xlim(-0.02, 1.02)
    plt.ylim(-0.02, 1.02)
    plt.grid(alpha=0.3)
    plt.savefig("observer_strategy/" + type + rate + hit_get + ".jpg")
    plt.show()


if __name__ == "__main__":
    plot("ba", "0.5", "hitting rate", legend=True)
    plot("ba", "0.5", "getting rate")
    plot("ba", "1.0", "hitting rate")
    plot("ba", "1.0", "getting rate")

    plot("er", "0.5", "hitting rate", legend=True)
    plot("er", "0.5", "getting rate")
    plot("er", "1.0", "hitting rate")
    plot("er", "1.0", "getting rate")
