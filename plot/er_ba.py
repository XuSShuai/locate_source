import numpy as np
import matplotlib.pyplot as plt

# plt.rcParams["figure.figsize"] = (10, 7)

FOLDER_PATH = "./er_ba/"
COMMON_NAME = "100max_degreeTrue"
X_RANGE = [x/50 for x in range(50)][::2]
COLORS = ['bisque','lightgreen','slategrey','lightcoral','olivedrab',
          'orchid','cornflowerblue','hotpink','tomato','indigo']
symbols = ['o','v', '*','s','D','^','H', 'o', 'v', '*']
SYMBOLS_SIZE = 8

font = {'family': 'serif',
        'color': 'black',
        'weight': 'normal',
        'size': 13,
        "alpha": 0.8
        }

legned_font = {'family': 'serif',
        'size': 11,
        }


def plot(type, hit_or_get, legend=False, text="(a)"):
    fig, ax = plt.subplots()
    for i in range(10):
        file_name = FOLDER_PATH + type + COMMON_NAME + str((i + 1) / 10) + ".txt"
        data = np.loadtxt(file_name)
        if hit_or_get == "hitting rate":
            plt.plot(X_RANGE, data[:, 0][::2],
                     marker=symbols[i],
                     color=COLORS[i], alpha=0.818,
                     label=r"$\beta$=" + str((i+1)/10), ms=SYMBOLS_SIZE)
        if hit_or_get == "getting rate":
            plt.plot(X_RANGE, data[:, 1][::2],
                     marker=symbols[i],
                     color=COLORS[i], alpha=0.818,
                     label=r"$\beta$=" + str((i+1)/10), ms=SYMBOLS_SIZE)
    if legend:
       plt.legend(shadow=True, prop=legned_font)
    plt.xlim(-0.0, 1.0)
    plt.ylim(-0.0, 1.0)
    plt.title(type.upper() + " network", fontdict=font)
    plt.grid(alpha=0.3)
    plt.ylabel(hit_or_get, fontdict=font)
    plt.xlabel("observers proportion", fontdict=font)
    ax.spines['left'].set_color('gray')
    ax.spines['right'].set_color('gray')
    ax.spines['bottom'].set_color('gray')
    ax.spines['top'].set_color('gray')
    plt.text(-0.15, 1.1, text, fontdict=font)
    plt.savefig("./er_ba/" + type + hit_or_get + ".eps")
    plt.show()


if __name__ == "__main__":
    plot("er", hit_or_get="hitting rate")
    plot("er", hit_or_get="getting rate", text="(b)")
    plot("ba", hit_or_get="hitting rate", text="(c)")
    plot("ba", hit_or_get="getting rate", text="(d)", legend=True)
