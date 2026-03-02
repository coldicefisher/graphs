from graphs.core.graph import Graph
from graphs.core.node import Node
from graphs.core.edge import Edge

from graphs.mst.prims import prims
from graphs.connectivity.structural import find_bridges, DFSTreeStats, find_articulation_points

# Load the data //////////////////////////

# Track the edges loaded into a list of tuples.
loaded_edges = list()
# We use a set to track the unique nodes loaded.
loaded_nodes = set()

with open("assignment2/Program2_Input.csv", "r") as f:
    for line in f:
        line = line.strip()

        
        x, y = line.split(",")
        x = int(x)
        y = int(y)
        loaded_edges.append((x, y))
        loaded_nodes.add(x)
        loaded_nodes.add(y)

    
    
with open("assignment2/assignment2_output.txt", "w") as fh:  
    # Create the graph ///////////////////////
    graph = Graph(num_nodes=len(loaded_nodes), undirected=True)

    # Iterate through the loaded edges and add them to the graph.
    for x, y in loaded_edges:
        graph.insert_edge(x, y, weight=1.0)
        
    print(f"Graph has {graph.num_nodes} nodes and {len(graph.make_edge_list())} edges.")
    fh.write(f"Graph has {graph.num_nodes} nodes and {len(graph.make_edge_list())} edges.\n")
    # for edge in graph.make_edge_list():
    #     print(f"{edge.from_node} -> {edge.to_node}")


    # Use prims algo to determine if the graph is connected. If the graph is disconnected, prims will return None.
    mst = prims(graph)

    if mst is None:
        print("Graph is disconnected.")
        fh.write("Graph is disconnected.\n")
    else:
        print("Graph is connected.")
        fh.write("Graph is connected.\n")
        
    tree_stats = DFSTreeStats(graph.num_nodes)

    # We can use the find_bridges function to find the bridges
    bridges = find_bridges(graph)
    print("")
    print("*" * 20)
    fh.write("\n" + "*" * 20 + "\n")
    print(f"Bridges in the graph:")
    fh.write("Bridges in the graph:\n")
    for edge in bridges:
        print(f"{edge.from_node} -> {edge.to_node}")
        fh.write(f"{edge.from_node} -> {edge.to_node}\n")
        
        
    # Get the articulation points in the graph.
    articulation_points = find_articulation_points(graph)

    print("")
    print("*" * 20)
    print("\nArticulation Points:")
    fh.write("\n" + "*" * 20 + "\n")
    fh.write("Articulation Points:\n")
    if not articulation_points:
        print("No articulation points found.")
        fh.write("No articulation points found.\n")
    else:
        for node in sorted(articulation_points):
            print(node)
            fh.write(f"{node}\n")
            
    print("")
    print("*" * 20)
    print("\nMinimum Spanning Tree Edges:")
    fh.write("\n" + "*" * 20 + "\n")
    fh.write("Minimum Spanning Tree Edges:\n")

    if mst is None:
        print("No MST (graph disconnected).")
        fh.write("No MST (graph disconnected).\n")
    else:
        total_weight = 0
        for edge in mst:
            print(f"{edge.from_node} -> {edge.to_node} (weight={edge.weight})")
            fh.write(f"{edge.from_node} -> {edge.to_node} (weight={edge.weight})\n")
            total_weight += edge.weight

        print(f"Total MST Weight: {total_weight}")
        fh.write(f"Total MST Weight: {total_weight}\n")