import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
plt.switch_backend("agg")


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
        print("is full connected: ", nx.is_connected(G))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True,
                node_size=np.array([x[1] for x in np.array(nx.degree(G))]) * 10,
                font_size=10)
        plt.show()
    return G


if __name__ == "__main__":
    pass
    G = load_empirical("./network_data/Celegans.data", show=False)
    G = load_empirical("./network_data/florida.data", show=False)
    G = load_empirical("./network_data/Metabolic.data", show=False)
    G = load_empirical("./network_data/USAir.data", show=False)