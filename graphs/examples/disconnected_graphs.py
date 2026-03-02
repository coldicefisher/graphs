from graphs.core.graph import Graph
from graphs.traversal.dfs_search import dfs_connected_components


def build_sample_graph():
    g = Graph(10, undirected=True)

    # Component 1
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(1, 2, 1.0)
    g.insert_edge(2, 5, 1.0)
    g.insert_edge(5, 4, 1.0)
    g.insert_edge(4, 3, 1.0)
    g.insert_edge(3, 0, 1.0)

    # Component 2
    g.insert_edge(6, 7, 1.0)
    g.insert_edge(7, 8, 1.0)
    g.insert_edge(8, 9, 1.0)

    return g


def dump_graph(g: Graph):
    print("=" * 50)
    print("GRAPH DATA DUMP")
    print("=" * 50)

    print(f"\nTotal Nodes: {g.num_nodes}")
    print(f"Undirected: {g.undirected}")

    print("\n--- Nodes ---")
    for node in g.nodes:
        print(f"Node {node.index}")

    print("\n--- Edges (Unique List) ---")
    seen = set()
    for node in g.nodes:
        for edge in node.get_edge_list():
            pair = tuple(sorted((edge.from_node, edge.to_node)))
            if pair not in seen:
                seen.add(pair)
                print(f"{pair[0]} <--> {pair[1]}  weight={edge.weight}")

    print("\n--- Adjacency List ---")
    for node in g.nodes:
        neighbors = sorted(node.get_neighbors())
        print(f"{node.index}: {neighbors}")

    print("\n--- Connected Components ---")
    components = dfs_connected_components(g)

    groups = {}
    for node_index, comp_id in enumerate(components):
        groups.setdefault(comp_id, []).append(node_index)

    for comp_id, nodes in groups.items():
        print(f"Component {comp_id}: {nodes}")

    print("\n--- Degree of Each Node ---")
    for node in g.nodes:
        print(f"Node {node.index} degree = {node.num_edges()}")

    print("=" * 50)


def main():
    g = build_sample_graph()
    dump_graph(g)


if __name__ == "__main__":
    main()