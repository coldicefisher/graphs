from graphs.mst.prims import prims
from .load_weighted_graph import load_weighted_graph_from_file


def main():
    g = load_weighted_graph_from_file("graphs/examples/mst/mst_graph.txt")

    mst = prims(g)

    if mst is None:
        print("Graph is disconnected.")
        return

    total_weight = 0.0

    print("MST Edges:")
    for edge in mst:
        print(f"{edge.from_node} -> {edge.to_node}  weight={edge.weight}")
        total_weight += edge.weight

    print(f"\nTotal MST Weight = {total_weight}")


if __name__ == "__main__":
    main()