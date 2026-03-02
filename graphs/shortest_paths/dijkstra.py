# graphs/shortest_paths/dijkstra.py



import math
import queue

from graphs.core.graph import Graph
from graphs.core.priority_queue import PriorityQueue

def dijkstra(g: Graph, start: int) -> tuple[list, list]:
    dist = [math.inf] * g.num_nodes
    last = [-1] * g.num_nodes

    pq = PriorityQueue()

    dist[start] = 0.0
    pq.enqueue(start, 0.0)

    while not pq.is_empty():
        current = pq.dequeue()

        for edge in g.nodes[current].get_edge_list():
            neighbor = edge.to_node
            new_cost = dist[current] + edge.weight

            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                last[neighbor] = current
                if pq.in_queue(neighbor):
                    pq.update_priority(neighbor, new_cost)
                else:
                    pq.enqueue(neighbor, new_cost)

    return dist, last

