# graphs/examples/mst/run_kruskals.py

from graphs.mst.kruskals import kruskals
from graphs.examples.mst.load_weighted_graph import load_weighted_graph_from_file


def main():
    g = load_weighted_graph_from_file("graphs/examples/mst/mst_graph.txt")

    print("=" * 50)
    print("Running Kruskal's Algorithm")
    print("=" * 50)

    mst = kruskals(g)

    if mst is None:
        print("Graph is disconnected — no spanning tree.")
        return

    print("\nMST Edges (in chosen order):")

    total_weight = 0.0
    for edge in mst:
        print(f"{edge.from_node} -- {edge.to_node}  weight={edge.weight}")
        total_weight += edge.weight

    print(f"\nTotal MST Weight = {total_weight}")
    print("=" * 50)


if __name__ == "__main__":
    main()