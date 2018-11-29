import matplotlib.pyplot as plt
import numpy as np


folder_pre = "./empirical_network/"
file_name = ["Celegans", "florida", "USAir", "Metabolic"]
file_pre = "max_degreeTrue"
file_post = ".txt"
X_RANGE = [x/50 for x in range(50)]
COLORS = ['bisque','lightgreen','slategrey','lightcoral','olivedrab',
          'orchid','cornflowerblue','hotpink','tomato','indigo']


def network_of(network_name, hit_or_get, legend = False):
    print(network_name)
    for id in range(1, 11, 1):
        file_path = folder_pre + network_name + "/" + network_name\
                    + file_pre + str(id/10) + file_post
        data = np.loadtxt(file_path)
        if hit_or_get == "hitting rate":
            plt.plot(X_RANGE, data[:,0], "-o", ms=5, label="beta="+str(id/10),
                     alpha=0.718, color=COLORS[id - 1])
        elif hit_or_get == "getting rate":
            plt.plot(X_RANGE, data[:,1], "-o", ms=5, label="beta="+str(id/10),
                     alpha=0.718, color=COLORS[id - 1])

    if legend:
        plt.legend(shadow=0.4)
    plt.xlim(-0.02, 1.02)
    plt.ylim(-0.02, 1.02)
    plt.title(network_name, fontsize=15)
    plt.xlabel("observer proportion", fontsize=13)
    plt.ylabel(hit_or_get, fontsize=14)
    plt.grid(alpha=0.4)
    plt.savefig("./empirical_network/" + hit_or_get + network_name + ".jpg")
    plt.show()


if __name__ == "__main__":
    for hg in ["hitting rate", "getting rate"]:
       for index, file in enumerate(file_name):
            if index == 0:
                network_of(file, hg, legend=True)
            else:
                network_of(file, hg)
