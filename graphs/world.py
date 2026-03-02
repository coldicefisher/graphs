# graphs/world.py


import math
import queue
from graphs.core.priority_queue import PriorityQueue

from graphs.core.graph import Graph
from graphs.core.node import Node
from graphs.core.edge import Edge


from graphs.traversal.bfs_search import breadth_first_search
from graphs.traversal.dfs_search import depth_first_search_path, topological_dfs

from typing import Union



class World:
    def __init__(self, g: Graph, start_ind: int, goal_ind: int):
        self.g: Graph = g
        self.start_ind: int = start_ind
        self.goal_ind: int = goal_ind
        
        
    def get_num_states(self) -> int:
        return self.g.num_nodes
    
    def is_goal(self, state: int) -> bool:
        return state == self.goal_ind
    
    
    def get_neighbors(self, state: int) -> set:
        return self.g.nodes[state].get_neighbors()
    
    
    def get_cost(self, from_state: int, to_state: int) -> float:
        if not self.g.is_edge(from_state, to_state):
            return math.inf
        
        return self.g.get_edge(from_state, to_state).weight
    
    
    def get_heuristic(self, state: int) -> float:
        pos1 = self.g.nodes[state].label
        pos2 = self.g.nodes[self.goal_ind].label
        return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)
    
    
    def get_start_index(self) -> int:
        return self.start_ind
    
    
def astar_dynamic(w: World) -> list:
    visited: dict = {}
    last: dict = {}
    cost: dict = {}
    pq: PriorityQueue = PriorityQueue()
    visited_goal: bool = False
    
    start: int = w.get_start_index()
    visited[start] = False
    last[start] = -1
    pq.enqueue(start, w.get_heuristic(start))
    cost[start] = 0.0
    
    while not pq.is_empty() and not visited_goal:
        index: int = pq.dequeue()
        visited[index] = True
        visited_goal = w.is_goal(index)
        
        for other in w.get_neighbors(index):
            c: float = w.get_cost(index, other)
            h: float = w.get_heuristic(other)
            
            if other not in visited:
                visited[other] = False
                cost[other] = cost[index] + c
                last[other] = index
                pq.enqueue(other, cost[other] + h)
            elif cost[other] > cost[index] + c:
                cost[other] = cost[index] + c
                last[other] = index
                pq.update_priority(other, cost[other] + h)
                
    return last
    
    
    
def is_topo_ordered(g: Graph, ordering: list) -> bool:
    if len(ordering) != g.num_nodes:
        return False
    
    index_to_pos: list = [-1] * g.num_nodes
    for pos in range(g.num_nodes):
        current: int = ordering[pos]
        if index_to_pos[current] != -1:
            return False
        index_to_pos[current] = pos
        
    for n in g.nodes:
        for edge in n.get_edge_list():
            if index_to_pos[edge.to_node] <= index_to_pos[edge.from_node]:
                return False
            
    return True



def Kahns(g: Graph) -> list:
    count: list = [0] * g.num_nodes
    s: list = []
    result: list = []
    
    for current in g.nodes:
        for edge in current.get_edge_list():
            count[edge.to_node] = count[edge.to_node] + 1
    
    for current in g.nodes:
        if count[current.index] == 0:
            s.append(current.index)
        
            
    while len(s) > 0:
        current_index: int = s.pop()
        result.append(current_index)

        for edge in g.nodes[current_index].get_edge_list():
            count[edge.to_node] -= 1
            if count[edge.to_node] == 0:
                s.append(edge.to_node)

    return result        
                
    
def check_cycle_kehns(g: Graph) -> bool:
    result: list = Kahns(g)
    if len(result) == g.num_nodes:
        return False
    
    return True



def sort_forward_pointers(options: list) -> list:
    num_nodes: int = len(options)
    g: Graph = Graph(num_nodes)
    for current in range(num_nodes):
        for next_index in options[current]:
            if next_index != -1:
                g.insert_edge(current, next_index, 1.0)
                
    return Kahns(g)