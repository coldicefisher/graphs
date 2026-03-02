# graphs/mst/kruskals.py

from graphs.core.graph import Graph
from graphs.core.node import Node
from graphs.core.edge import Edge

import random
from typing import Union
import math

from graphs.core.union_find import UnionFind


def kruskals(g: Graph) -> Union[list, None]:
    djs: UnionFind = UnionFind(g.num_nodes)
    all_edges: list = []
    mst_edges: list = []

    for idx in range(g.num_nodes):
        for edge in g.nodes[idx].get_edge_list():
            if edge.to_node > edge.from_node:
                all_edges.append(edge)

    all_edges.sort(key=lambda edge: edge.weight)

    for edge in all_edges:
        if djs.are_disjoint(edge.to_node, edge.from_node):
            mst_edges.append(edge)
            djs.union_sets(edge.to_node, edge.from_node)

    if djs.num_disjoint_sets == 1:
        return mst_edges
    else:
        return None
    
    
    
def randomized_kruskals(g: Graph) -> list:
    djs: UnionFind = UnionFind(g.num_nodes)
    all_edges: list = []
    maze_edges: list = []
    
    for idx in range(g.num_nodes):
        for edge in g.nodes[idx].get_edge_list():
            if edge.to_node > edge.from_node:
                all_edges.append(edge)

    while djs.num_disjoint_sets > 1 and all_edges:
        edge_ind = random.randint(0, len(all_edges) - 1)
        new_edge = all_edges.pop(edge_ind)

        if djs.are_disjoint(new_edge.to_node, new_edge.from_node):
            maze_edges.append(new_edge)
            djs.union_sets(new_edge.to_node, new_edge.from_node)
        
    # while djs.num_disjoint_sets > 1:
    #     num_edges: int = len(all_edges)
    #     edge_ind: int = random.randint(0, num_edges - 1)
    #     new_edge: Edge = all_edges[edge_ind]
        
        
    #     if djs.num_disjoint_sets > 1:
    #         num_edges: int = len(all_edges)
    #         edge_ind: int = random.randint(0, num_edges - 1)
    #         new_edge: Edge = all_edges.pop(edge_ind)
            
            if djs.are_disjoint(new_edge.to_node, new_edge.from_node):
                maze_edges.append(new_edge)
                djs.union_sets(new_edge.to_node, new_edge.from_node)
                
    return maze_edges

