from graphs.core.graph import Graph


def load_weighted_graph_from_file(filename: str, undirected=True) -> Graph:
    edges = []
    max_node = 0

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            u, v, w = line.split()
            u = int(u)
            v = int(v)
            w = float(w)

            edges.append((u, v, w))
            max_node = max(max_node, u, v)

    g = Graph(max_node + 1, undirected=undirected)

    for u, v, w in edges:
        g.insert_edge(u, v, w)

    return g