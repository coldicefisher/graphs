


# *******************************************************************************
# assignment2/main.py
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
        
        
        

# *******************************************************************************
# graphs/connectivity/structural.py

from graphs.core.graph import Graph
from graphs.core.edge import Edge
from graphs.core.node import Node

    
class DFSTreeStats:
    def __init__(self, num_nodes: int):
        self.parent: list = [-1] * num_nodes
        self.next_order_index: int = 0
        self.order: list = [-1] * num_nodes
        self.lowest: list = [-1] * num_nodes
        
        
    def set_order_index(self, node_index: int):
        self.order[node_index] = self.next_order_index
        self.next_order_index += 1
        self.lowest[node_index] = self.order[node_index]
        
        
def bridge_finding_dfs(g: Graph, index: int, stats: DFSTreeStats, results: list):
    stats.set_order_index(index)
    
    for edge in g.nodes[index].get_sorted_edge_list():
        neighbor: int = edge.to_node
        if stats.order[neighbor] == -1:
            stats.parent[neighbor] = index
            bridge_finding_dfs(g, neighbor, stats, results)
            
            stats.lowest[index] = min(stats.lowest[index],
                                      stats.lowest[neighbor])
            
            if stats.lowest[neighbor] > stats.order[index]:
                results.append(edge)
                
        elif neighbor != stats.parent[index]:
            stats.lowest[index] = min(stats.lowest[index], 
                                      stats.order[neighbor])
                                            
                                            
def find_bridges(g: Graph) -> list:
    results: list = []
    stats: DFSTreeStats = DFSTreeStats(g.num_nodes)
    
    for index in range(g.num_nodes):
        if stats.order[index] == -1:
            bridge_finding_dfs(g, index, stats, results)
            
    return results


def articulation_point_dfs(g: Graph, index: int, stats: DFSTreeStats, results: set):
    stats.set_order_index(index)
    
    for edge in g.nodes[index].get_edge_list():
        neighbor: int = edge.to_node
        if stats.order[neighbor] == -1:
            stats.parent[neighbor] = index
            articulation_point_dfs(g, neighbor, stats, results)
            
            stats.lowest[index] = min(stats.lowest[index],
                                      stats.lowest[neighbor])
            
            # if stats.parent[index] >= stats.order[index]:
            if stats.lowest[neighbor] >= stats.order[index]:
                results.add(index)
                
        elif neighbor != stats.parent[index]:
            stats.lowest[index] = min(stats.lowest[index], 
                                      stats.order[neighbor])
            
            
            
def articulation_point_root(g: Graph, root: int, stats: DFSTreeStats, results: set):
    stats.set_order_index(root)
    num_subtrees: int = 0
    
    for edge in g.nodes[root].get_edge_list():
        neighbor: int = edge.to_node
        if stats.order[neighbor] == -1:
            stats.parent[neighbor] = root
            articulation_point_dfs(g, neighbor, stats, results)
            num_subtrees += 1
            
    if num_subtrees >= 2:
        results.add(root)
        
    

def find_articulation_points(g: Graph) -> set:
    stats: DFSTreeStats = DFSTreeStats(g.num_nodes)
    results: set = set()
    
    for index in range(g.num_nodes):
        if stats.order[index] == -1:
            articulation_point_root(g, index, stats, results)
            
    return results

# *******************************************************************************

# graphs/mst/prims.py

from graphs.core.priority_queue import PriorityQueue

from graphs.core.graph import Graph
from graphs.core.node import Node
from graphs.core.edge import Edge

from typing import Union

import math



    
    
    

    
def prims(g: Graph) -> Union[list, None]:
    pq: PriorityQueue = PriorityQueue()
    last: list = [-1] * g.num_nodes
    mst_edges: list = []
    
    pq.enqueue(0, 0.0)
    for i in range(1, g.num_nodes):
        pq.enqueue(i, float('inf'))
        
    while not pq.is_empty():
        index: int = pq.dequeue()
        current: Node = g.nodes[index]
        
        if last[index] != -1:
            mst_edges.append(current.get_edge(last[index]))
        elif index != 0:
            return None
        
        for edge in current.get_edge_list():
            neighbor: int = edge.to_node
            if pq.in_queue(neighbor):
                
                if edge.weight < pq.get_priority(neighbor):
                    pq.update_priority(neighbor, edge.weight)
                    last[neighbor] = index
                    
                    
    return mst_edges


# *******************************************************************************

# graphs/graph.py

from graphs.core.node import Node
from graphs.core.edge import Edge

from typing import Union


class Graph:
    def __init__(self, num_nodes: int, undirected: bool=False):
        self.num_nodes: int = num_nodes
        self.undirected: bool = undirected
        self.nodes: list = [Node(j) for j in range(num_nodes)]
        
        
    def get_edge(self, from_node: int, to_node: int) -> Union[Edge, None]:
        if from_node < 0 or from_node >= self.num_nodes:
            raise IndexError
        
        return self.nodes[from_node].get_edge(to_node)
    
    
    def is_edge(self, from_node: int, to_node: int) -> bool:
        return self.get_edge(from_node, to_node) is not None
    
    
    def make_edge_list(self) -> list:
        all_edges: list = []
        for node in self.nodes:
            for edge in node.edges.values():
                all_edges.append(edge)
                
        return all_edges
    
    
    def insert_edge(self, from_node: int, to_node: int, weight: float):
        if from_node < 0 or from_node >= self.num_nodes:
            raise IndexError
        
        self.nodes[from_node].add_edge(to_node, weight)
        
        if self.undirected:
            self.nodes[to_node].add_edge(from_node, weight)
            
            
    def remove_edge(self, from_node: int, to_node: int):
        if from_node < 0 or from_node >= self.num_nodes:
            raise IndexError
        
        if to_node < 0 or to_node >= self.num_nodes:
            raise IndexError
        
        self.nodes[from_node].remove_edge(to_node)
        
        if self.undirected:
            self.nodes[to_node].remove_edge(from_node)
            
            
    def make_copy(self) -> 'Graph':
        g2: Graph = Graph(self.num_nodes, undirected=self.undirected)
        
        for node in self.nodes:
            g2.nodes[node.index].label = node.label
            for edge in node.edges.values():
                if not self.undirected or edge.to_node > edge.from_node:
                    g2.insert_edge(edge.from_node, edge.to_node, edge.weight)
                
        return g2
    
    
    
    def get_in_neighbors(self, target: int) -> set:
        neighbors: set = set()
        for node in self.nodes:
            if target in node.edges:
                neighbors.add(node.index)
        
        return neighbors
    
    
    def clustering_coefficient(self, node_index: int) -> float:
        
        
        if not self.undirected:
            raise ValueError("Graph must be undirected")
        
        neighbors: set = self.nodes[node_index].get_neighbors()
        num_neighbors: int = len(neighbors)
        
        count: int = 0
        for n1 in neighbors:
            for edge in self.nodes[n1].get_edge_list():
                if edge.to_node > n1 and edge.to_node in neighbors:
                    count += 1
                    
        total_possible = (num_neighbors * (num_neighbors - 1)) / 2.0
        if total_possible == 0:
            return 0.0
        
        return count / total_possible
    
    
    def average_clustering_coefficient(self) -> float:
        total: float = 0.0
        for n in range(self.num_nodes):
            total += self.clustering_coefficient(n)
            
        if self.num_nodes == 0:
            return 0.0
        
        return total / self.num_nodes
    
    
    def make_undirected_neighborhood_subgraph(self, node_index: int, closed: bool):
        if not self.undirected:
            raise ValueError("Graph must be undirected")
        
        nodes_to_use: set = self.nodes[node_index].get_neighbors()
        if closed:
            nodes_to_use.add(node_index)
            
        index_map: dict = {}
        
        for new_index, old_index in enumerate(nodes_to_use):
            index_map[old_index] = new_index
            
        g_new: Graph = Graph(len(nodes_to_use), undirected=True)
        for n in nodes_to_use:
            for edge in self.nodes[n].get_edge_list():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                if edge.to_node in nodes_to_use and edge.to_node > n:
                    ind1_new = index_map[n]
                    ind2_new = index_map[edge.to_node]
                    g_new.insert_edge(ind1_new, ind2_new, edge.weight)
                    
                    
        return g_new
    
    
    def insert_node(self, label=None) -> Node:
        new_node: Node = Node(self.num_nodes, label)
        self.nodes.append(new_node)
        self.num_nodes += 1
        return new_node









