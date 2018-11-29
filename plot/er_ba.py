import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (10, 7)

FOLDER_PATH = "./er_ba/"
COMMON_NAME = "100max_degreeTrue"
X_RANGE = [x/50 for x in range(50)]
COLORS = ['bisque','lightgreen','slategrey','lightcoral','olivedrab',
          'orchid','cornflowerblue','hotpink','tomato','indigo']
symbols = ['o-','v-', '*-','s-','D-','^-','H-', 'o-', 'v-', '*-']


def plot(type, hit_or_get, legend=False):
    for i in range(10):
        file_name = FOLDER_PATH + type + COMMON_NAME + str((i + 1) / 10) + ".txt"
        data = np.loadtxt(file_name)
        if hit_or_get == "hitting rate":
            plt.plot(X_RANGE, data[:, 0], "-x", color=COLORS[i], alpha=0.818,
                     label="beta=" + str((i+1)/10))
        if hit_or_get == "getting rate":
            plt.plot(X_RANGE, data[:, 1], "-x", color=COLORS[i], alpha=0.818,
                     label="beta=" + str((i+1)/10))
    if legend:
       plt.legend(shadow=True, fontsize=14)
    plt.xlim(-0.02, 1.02)
    plt.ylim(-0.02, 1.02)
    plt.title(type + " network", fontsize=20)
    plt.grid(alpha=0.3)
    plt.ylabel(hit_or_get, fontsize=16)
    plt.xlabel("observers proportion", fontsize=15)
    plt.savefig("./er_ba/" + type + hit_or_get + ".jpg")
    plt.show()


if __name__ == "__main__":
    plot("er", hit_or_get="hitting rate", legend=True)
    plot("er", hit_or_get="getting rate")
    plot("ba", hit_or_get="hitting rate")
    plot("ba", hit_or_get="getting rate")
