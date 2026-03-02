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