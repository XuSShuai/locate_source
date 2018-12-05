import matplotlib.pyplot as plt
import numpy as np


folder_pre = "./empirical_network/"
file_name = ["Celegans", "florida", "USAir", "Metabolic"]
file_pre = "max_degreeTrue"
file_post = ".txt"
X_RANGE = [x/50 for x in range(50)][::2]
COLORS = ['bisque','lightgreen','slategrey','lightcoral','olivedrab',
          'orchid','cornflowerblue','hotpink','tomato','indigo']

font = {'family': 'serif',
        'color': 'black',
        'weight': 'normal',
        'size': 13,
        "alpha": 0.8
        }

legned_font = {'family': 'serif',
        'size': 11,
        }


def network_of(network_name, hit_or_get, legend=False, text="(A)"):
    print(network_name)
    fig, ax = plt.subplots()
    for id in range(1, 11, 1):
        file_path = folder_pre + network_name + "/" + network_name\
                    + file_pre + str(id/10) + file_post
        data = np.loadtxt(file_path)
        if hit_or_get == "hitting rate":
            plt.plot(X_RANGE, data[:,0][::2], "-", ms=6, label=r"$\beta$="+str(id/10),
                     alpha=0.618, color=COLORS[id - 1], linewidth=1.8)
        elif hit_or_get == "getting rate":
            plt.plot(X_RANGE, data[:,1][::2], "-", ms=6, label=r"$\beta$="+str(id/10),
                     alpha=0.618, color=COLORS[id - 1], linewidth=1.8)

    if legend:
        plt.legend(shadow=0.4, prop=legned_font)
    plt.xlim(-0.0, 1.0)
    plt.ylim(-0.0, 1.0)
    plt.title(network_name if network_name != "florida" else "FWFW", fontdict=font)
    plt.xlabel("observer proportion", fontdict=font)
    plt.ylabel(hit_or_get, fontdict=font)
    plt.grid(alpha=0.4)
    ax.spines['left'].set_color('gray')
    ax.spines['right'].set_color('gray')
    ax.spines['bottom'].set_color('gray')
    ax.spines['top'].set_color('gray')
    plt.text(-0.15, 1.1, text, fontdict=font)
    plt.savefig("./empirical_network/" + hit_or_get + network_name + ".eps")
    plt.show()


if __name__ == "__main__":
    for out_index, hg in enumerate(["hitting rate", "getting rate"]):
       for in_index, file in enumerate(file_name):
            if in_index == 3 and hg == "getting rate":
                network_of(file, hg, legend=True, text="("+chr(97+((out_index*(len(file_name)))+in_index))+")")
            else:
                network_of(file, hg, text="("+chr(97+((out_index*(len(file_name)))+in_index))+")")
