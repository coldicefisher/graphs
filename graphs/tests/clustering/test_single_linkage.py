# tests/clustering/test_single_linkage.py

import pytest
from graphs.clustering.single_linkage import (
    single_linkage_clustering,
    Point
)



# Basic Structure Tests


def test_empty_points():
    result = single_linkage_clustering([])
    assert result == []


def test_single_point():
    result = single_linkage_clustering([Point(0, 0)])
    assert result == []


def test_two_points():
    points = [Point(0, 0), Point(3, 4)]  # distance = 5
    result = single_linkage_clustering(points)

    assert len(result) == 1
    assert result[0].dist == 5.0



# Simple Triangle


def test_triangle_clustering():
    # Right triangle
    points = [
        Point(0, 0),  # A
        Point(1, 0),  # B
        Point(0, 1),  # C
    ]

    result = single_linkage_clustering(points)

    # MST should have n - 1 edges
    assert len(result) == 2

    distances = sorted(link.dist for link in result)

    # Shortest two edges are 1 and 1
    assert distances == [1.0, 1.0]



# Line of Points


def test_linear_points():
    points = [
        Point(0, 0),
        Point(1, 0),
        Point(2, 0),
        Point(3, 0),
    ]

    result = single_linkage_clustering(points)

    assert len(result) == 3  # n - 1

    distances = sorted(link.dist for link in result)
    assert distances == [1.0, 1.0, 1.0]



# Square Points


def test_square_points():
    # 4 points forming square
    points = [
        Point(0, 0),
        Point(1, 0),
        Point(0, 1),
        Point(1, 1),
    ]

    result = single_linkage_clustering(points)

    assert len(result) == 3  # n - 1

    # All shortest edges are length 1
    distances = sorted(link.dist for link in result)
    assert distances[0] == 1.0



# Verify No Cycles


def test_no_cycles_property():
    points = [
        Point(0, 0),
        Point(1, 0),
        Point(0, 1),
        Point(2, 2),
    ]

    result = single_linkage_clustering(points)

    # Ensure exactly n - 1 links
    assert len(result) == len(points) - 1