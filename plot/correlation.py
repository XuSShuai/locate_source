import matplotlib.pyplot as plt
import numpy as np
import os.path
import glob

X_RANGE = [x/50 for x in range(50)][::2]
POINT_SIZE = 80
ALPHA = 0.718
plt.rcParams["figure.figsize"] = (4.5, 6)

font = {'family': 'serif',
        'color': 'black',
        'weight': 'normal',
        'size': 13,
        "alpha": 0.8
        }

legned_font = {'family': 'serif',
        'size': 12,
        }


def load_data():
    COS_FOLD = "./er_ba"
    PEARSON_FOLD = "./er_ba_pearson"
    glob_file_pattern = os.path.join(COS_FOLD, "ba*.txt")
    cos_file_list = glob.glob(glob_file_pattern)
    cos_result = []
    for file in cos_file_list:
        cos_result.append(np.loadtxt(file, dtype=np.float32, delimiter="\t"))

    glob_file_pattern = os.path.join(PEARSON_FOLD, "ba*.txt")
    pearson_file_list = glob.glob(glob_file_pattern)
    pearson_result = []
    for file in pearson_file_list:
        pearson_result.append(np.loadtxt(file, dtype=np.float32, delimiter="\t"))

    return cos_result, pearson_result


def plot():
    cos, pearson = load_data()
    print(len(cos))
    for i in range(10):
        if i == 4:
            fig, ax = plt.subplots()
            plt.scatter(X_RANGE, cos[i][::2, 0], marker="^", color="black", s=POINT_SIZE,
                        alpha=ALPHA, label="getting rate, cosine similarity")
            plt.scatter(X_RANGE, cos[i][::2, 1], marker="o", color="black", s=POINT_SIZE,
                        alpha=ALPHA, label="hitting rate, cosine similarity")
            plt.scatter(X_RANGE, pearson[i][::2, 0], marker="^", color="red", s=POINT_SIZE,
                        alpha=ALPHA, label="getting rate, pearson similarity")
            plt.scatter(X_RANGE, pearson[i][::2, 1], marker="o", color="red", s=POINT_SIZE,
                        alpha=ALPHA, label="hitting rate, pearson similarity")
        else:
            fig, ax = plt.subplots()
            plt.scatter(X_RANGE, cos[i][::2, 0], marker="^", color="black", s=POINT_SIZE, alpha=ALPHA)
            plt.scatter(X_RANGE, cos[i][::2, 1], marker="o", color="black", s=POINT_SIZE, alpha=ALPHA)
            plt.scatter(X_RANGE, pearson[i][::2, 0], marker="^", color="red", s=POINT_SIZE, alpha=ALPHA)
            plt.scatter(X_RANGE, pearson[i][::2, 1], marker="o", color="red", s=POINT_SIZE, alpha=ALPHA)
        if i == 4:
            plt.legend(shadow=True, prop=legned_font)
        plt.title(r"$\beta$=" + str((i+1)/10), fontdict=font)
        plt.xlim(-0., 1.)
        plt.xticks(fontsize=12, alpha=ALPHA)
        plt.ylim(-0., 1.)
        plt.yticks(fontsize=12, alpha=ALPHA)
        plt.grid(alpha=0.3)
        ax.spines['left'].set_color('gray')
        ax.spines['right'].set_color('gray')
        ax.spines['bottom'].set_color('gray')
        ax.spines['top'].set_color('gray')
        plt.ylabel("h/g", fontdict=font)
        plt.xlabel("observers proportion", fontdict=font)
        plt.tight_layout()
        plt.savefig("./correlation/" + str(i) + ".jpg")
        plt.show()

if __name__ == "__main__":
    plot()