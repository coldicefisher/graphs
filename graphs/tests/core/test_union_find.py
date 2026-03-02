# tests/core/test_union_find.py

import pytest
from graphs.core.union_find import UnionFind



# Initialization


def test_initial_state():
    uf = UnionFind(5)

    # Each element is its own parent
    for i in range(5):
        assert uf.find(i) == i

    assert uf.num_disjoint_sets == 5



# Basic Union Behavior


def test_single_union():
    uf = UnionFind(4)

    uf.union(0, 1)

    assert uf.find(0) == uf.find(1)
    assert uf.num_disjoint_sets == 3


def test_multiple_unions():
    uf = UnionFind(5)

    uf.union(0, 1)
    uf.union(1, 2)

    # All should share same root
    root = uf.find(0)
    assert uf.find(1) == root
    assert uf.find(2) == root

    assert uf.num_disjoint_sets == 3


def test_union_already_connected_returns_false():
    uf = UnionFind(3)

    assert uf.union(0, 1) is True
    assert uf.union(0, 1) is False  # already connected

    assert uf.num_disjoint_sets == 2



# Disjoint Check


def test_are_disjoint():
    uf = UnionFind(4)

    assert uf.are_disjoint(0, 1) is True

    uf.union(0, 1)

    assert uf.are_disjoint(0, 1) is False
    assert uf.are_disjoint(0, 2) is True



# Path Compression Behavior


def test_path_compression_effect():
    uf = UnionFind(5)

    # Create chain: 0-1-2-3
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(2, 3)

    root_before = uf.parent[3]

    # Force path compression
    uf.find(3)

    root_after = uf.parent[3]

    # After compression, parent should be direct root
    assert root_after == uf.find(0)



# Rank Behavior


def test_union_by_rank():
    uf = UnionFind(4)

    uf.union(0, 1)
    uf.union(2, 3)

    # Now union the two trees
    uf.union(0, 2)

    root = uf.find(0)

    assert uf.find(1) == root
    assert uf.find(2) == root
    assert uf.find(3) == root

    assert uf.num_disjoint_sets == 1



# Large Union Scenario


def test_full_union():
    n = 10
    uf = UnionFind(n)

    for i in range(n - 1):
        uf.union(i, i + 1)

    assert uf.num_disjoint_sets == 1

    root = uf.find(0)
    for i in range(n):
        assert uf.find(i) == root