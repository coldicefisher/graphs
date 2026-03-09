"""
Chapter 11: Union-Find
Demonstrates the Union-Find (Disjoint Set Union) data structure.
"""

from graphs.core.union_find import UnionFind


def basic_union_find():
    """Basic union-find operations."""
    print("=== Basic Union-Find ===")
    uf = UnionFind(6)

    print(f"Initial disjoint sets: {uf.num_disjoint_sets}")

    uf.union(0, 1)
    uf.union(2, 3)
    print(f"After union(0,1) and union(2,3): {uf.num_disjoint_sets} sets")

    print(f"0 and 1 disjoint? {uf.are_disjoint(0, 1)}")
    print(f"0 and 2 disjoint? {uf.are_disjoint(0, 2)}")

    uf.union(1, 3)
    print(f"After union(1,3): {uf.num_disjoint_sets} sets")
    print(f"0 and 3 in same set? {not uf.are_disjoint(0, 3)}")
    print()


def path_compression_demo():
    """Show how find with path compression flattens the tree."""
    print("=== Path Compression ===")
    uf = UnionFind(5)

    # Build a chain: 0->1->2->3->4
    uf.union(3, 4)
    uf.union(2, 3)
    uf.union(1, 2)
    uf.union(0, 1)

    print(f"Parents before find: {uf.parent}")

    # find(0) triggers path compression
    root = uf.find(0)
    print(f"Root of 0: {root}")
    print(f"Parents after find(0): {uf.parent}")
    print()


def connected_components_via_union_find():
    """Use union-find to track connected components as edges are added."""
    print("=== Connected Components via Union-Find ===")
    uf = UnionFind(6)
    edges = [(0, 1), (2, 3), (4, 5), (1, 2), (3, 4)]

    for u, v in edges:
        was_disjoint = uf.are_disjoint(u, v)
        uf.union(u, v)
        print(f"Added edge ({u},{v}): "
              f"merged={'yes' if was_disjoint else 'no'}, "
              f"components={uf.num_disjoint_sets}")
    print()


def main():
    basic_union_find()
    path_compression_demo()
    connected_components_via_union_find()


if __name__ == "__main__":
    main()
