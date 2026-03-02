# graphs/clustering/single_linkage.py

from graphs.core.union_find import UnionFind
import math


class Point:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y
        
    
    def distance(self, b) -> float:
        diff_x: float = (self.x - b.x)
        diff_y: float = (self.y - b.y)
        dist: float = math.sqrt(diff_x ** 2 + diff_y ** 2)
        return dist
    
    
    
class Link:
    def __init__(self, dist: float, id1: int, id2: int):
        self.dist: float = dist
        self.id1: int = id1
        self.id2: int = id2

    
def single_linkage_clustering(points: list) -> list:
    num_pts: int = len(points)
    djs: UnionFind = UnionFind(num_pts)
    all_links: list = []
    cluster_links: list = []
    
    for id1 in range(num_pts):
        for id2 in range(id1 + 1, num_pts):
            dist: float = points[id1].distance(points[id2])
            all_links.append(Link(dist, id1, id2))
            
            
    all_links.sort(key=lambda link: link.dist)
    
    for x in all_links:
        if djs.are_disjoint(x.id1, x.id2):
            cluster_links.append(x)
            djs.union_sets(x.id1, x.id2)
    
    return cluster_links

