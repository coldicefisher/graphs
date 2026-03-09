"""
Chapter 13: Clustering
Demonstrates single-linkage hierarchical clustering.
"""

from graphs.clustering.single_linkage import Point, single_linkage_clustering


def basic_clustering():
    """Cluster a set of 2D points using single-linkage clustering."""
    print("=== Single-Linkage Clustering ===")
    points = [
        Point(0.0, 0.0),
        Point(1.0, 0.0),
        Point(5.0, 0.0),
        Point(6.0, 0.0),
        Point(10.0, 0.0),
    ]

    links = single_linkage_clustering(points)

    print(f"Points: {[(p.x, p.y) for p in points]}")
    print(f"Clustering links (in merge order):")
    for link in links:
        print(f"  Point {link.id1} -- Point {link.id2} "
              f"(distance {link.dist:.2f})")
    print()


def two_cluster_example():
    """Points naturally form two clusters."""
    print("=== Two Natural Clusters ===")
    points = [
        Point(0.0, 0.0),
        Point(1.0, 1.0),
        Point(0.5, 0.5),
        Point(10.0, 10.0),
        Point(11.0, 11.0),
        Point(10.5, 10.5),
    ]

    links = single_linkage_clustering(points)

    print("Merge order:")
    for i, link in enumerate(links):
        print(f"  Step {i + 1}: merge {link.id1} and {link.id2} "
              f"(dist={link.dist:.2f})")

    # The last merge connects the two clusters
    print(f"\nLargest gap (between clusters): {links[-1].dist:.2f}")
    print()


def clustering_coefficient_example():
    """Demonstrate graph clustering coefficient."""
    print("=== Graph Clustering Coefficient ===")
    from graphs.core.graph import Graph

    # Triangle: perfect clustering
    g1 = Graph(3, undirected=True)
    g1.insert_edge(0, 1, 1.0)
    g1.insert_edge(1, 2, 1.0)
    g1.insert_edge(0, 2, 1.0)
    print(f"Triangle clustering coeff (node 0): {g1.clustering_coefficient(0)}")
    print(f"Triangle average: {g1.average_clustering_coefficient()}")

    # Star: zero clustering
    g2 = Graph(4, undirected=True)
    g2.insert_edge(0, 1, 1.0)
    g2.insert_edge(0, 2, 1.0)
    g2.insert_edge(0, 3, 1.0)
    print(f"Star clustering coeff (center): {g2.clustering_coefficient(0)}")
    print(f"Star average: {g2.average_clustering_coefficient()}")
    print()


def main():
    basic_clustering()
    two_cluster_example()
    clustering_coefficient_example()


if __name__ == "__main__":
    main()
