# graphs/core/union_find.py





class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n


    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]


    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # already connected

        # union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True
    

    def are_disjoint(self, x, y):
        return self.find(x) != self.find(y)

    
    def union_sets(self, x, y):
        self.union(x, y)


    @property
    def num_disjoint_sets(self):
        return len(set(self.find(x) for x in range(len(self.parent))))    


    

