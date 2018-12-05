import numpy as np
import matplotlib.pyplot as plt

ALPHA = 0.718

FOLDER_PATH = "./observer_strategy/"
strategy_list = [
    "max_betweenness",
    "max_closeness",
    "max_degree",
    "max_k_shell",
    "min_betweenness",
    "min_closeness",
    "min_degree",
    "min_k_shell",
    "random",
    "mix_degree",
]
symbols = ['o', 'v', '*', 's', 'D', '^', 'H', 'o', 'v', '*']
X_RANGE = [x/50 for x in range(50)][::2]
COLORS = ['bisque','lightgreen','slategrey','lightcoral',
          'olivedrab','cornflowerblue','silver', 'hotpink',
          'orchid', 'indigo']

font = {'family': 'serif',
        'color': 'black',
        'weight': 'normal',
        'size': 13,
        "alpha": 0.8
        }

legned_font = {'family': 'serif',
        'size': 12,
        }


def plot(type, rate, hit_get, legend=False, text="(A)"):
    fig, ax = plt.subplots()
    for index, strategy in enumerate(strategy_list):
        file_name = FOLDER_PATH + type + "100" + strategy + "True" + rate + ".txt"
        data = np.loadtxt(file_name)
        if hit_get == "hitting rate":
            plt.plot(X_RANGE, data[::2, 0], marker=symbols[index],
                     alpha = 0.518, color=COLORS[index], label=strategy, ms=10)
        if hit_get == "getting rate":
            plt.plot(X_RANGE, data[::2, 1], marker=symbols[index],
                     alpha = 0.518, color=COLORS[index], label=strategy, ms=10)
    plt.xlabel("observers proportion", fontdict=font)
    plt.ylabel(hit_get, fontdict=font)
    plt.title(r"$\beta$=" + rate, fontdict=font)
    if legend:
        plt.legend(shadow=True, prop=legned_font)
    plt.xlim(-0.0, 1.0)
    plt.ylim(-0.0, 1.0)
    plt.xticks(fontsize=12, alpha=ALPHA)
    plt.yticks(fontsize=12, alpha=ALPHA)
    plt.grid(alpha=0.3)
    ax.spines['left'].set_color('gray')
    ax.spines['right'].set_color('gray')
    ax.spines['bottom'].set_color('gray')
    ax.spines['top'].set_color('gray')
    plt.text(-0.15, 1.1, text, fontdict=font)
    plt.savefig("observer_strategy/" + type + rate + hit_get + ".eps")
    plt.show()


if __name__ == "__main__":
    plot("ba", "0.5", "hitting rate", text="(a)")
    plot("ba", "0.5", "getting rate", legend=True, text="(b)")
    plot("ba", "1.0", "hitting rate", text="(c)")
    plot("ba", "1.0", "getting rate", text="(d)")

    # plot("er", "0.5", "hitting rate", legend=True)
    # plot("er", "0.5", "getting rate")
    # plot("er", "1.0", "hitting rate")
    # plot("er", "1.0", "getting rate")
