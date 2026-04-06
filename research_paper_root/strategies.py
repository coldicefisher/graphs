"""
Active learning query strategies for graph-based label propagation.
"""

import numpy as np
from collections import deque


def binary_entropy(p):
    """Compute binary entropy H(p) = -p log(p) - (1-p) log(1-p)."""
    p = np.clip(p, 1e-12, 1.0 - 1e-12)
    return -p * np.log2(p) - (1 - p) * np.log2(1 - p)


def random_selection(f, unlabeled_indices, rng):
    """Select a random unlabeled node."""
    return rng.choice(unlabeled_indices)


def uncertainty_sampling(f, unlabeled_indices, rng):
    """Select the unlabeled node with highest predictive entropy."""
    entropies = binary_entropy(f[unlabeled_indices])
    # Break ties randomly
    max_entropy = np.max(entropies)
    candidates = unlabeled_indices[entropies >= max_entropy - 1e-12]
    return rng.choice(candidates)


def max_degree_selection(W, unlabeled_indices, rng):
    """Select the unlabeled node with highest weighted degree."""
    degrees = np.sum(W[unlabeled_indices, :], axis=1)
    max_deg = np.max(degrees)
    candidates = unlabeled_indices[degrees >= max_deg - 1e-12]
    return rng.choice(candidates)


def betweenness_centrality_selection(W, unlabeled_indices, rng):
    """Select the unlabeled node with highest betweenness centrality.

    Uses Brandes' algorithm on the weighted graph (shorter distance = stronger
    connection, so we convert weights to distances).
    """
    n = W.shape[0]
    bc = _brandes_betweenness(W, n)
    bc_unlabeled = bc[unlabeled_indices]
    max_bc = np.max(bc_unlabeled)
    candidates = unlabeled_indices[bc_unlabeled >= max_bc - 1e-12]
    return rng.choice(candidates)


def _brandes_betweenness(W, n):
    """Brandes' algorithm for betweenness centrality on a weighted graph."""
    # Convert weights to distances: d_ij = 1/w_ij for w_ij > 0
    # Use Dijkstra-style shortest paths
    bc = np.zeros(n)

    for s in range(n):
        # Single-source shortest paths from s
        S = []  # stack of nodes in order of non-decreasing distance
        P = [[] for _ in range(n)]  # predecessors
        sigma = np.zeros(n)  # number of shortest paths
        sigma[s] = 1.0
        dist = np.full(n, np.inf)
        dist[s] = 0.0
        delta = np.zeros(n)

        # Priority queue: (distance, node)
        import heapq
        Q = [(0.0, s)]
        visited = np.zeros(n, dtype=bool)

        while Q:
            d_v, v = heapq.heappop(Q)
            if visited[v]:
                continue
            visited[v] = True
            S.append(v)

            for w in range(n):
                if W[v, w] <= 0 or v == w:
                    continue
                edge_dist = 1.0 / W[v, w]
                new_dist = d_v + edge_dist
                if new_dist < dist[w] - 1e-12:
                    dist[w] = new_dist
                    sigma[w] = sigma[v]
                    P[w] = [v]
                    heapq.heappush(Q, (new_dist, w))
                elif abs(new_dist - dist[w]) < 1e-12:
                    sigma[w] += sigma[v]
                    P[w].append(v)

        # Back-propagation of dependencies
        while S:
            w = S.pop()
            for v in P[w]:
                if sigma[w] > 0:
                    delta[v] += (sigma[v] / sigma[w]) * (1.0 + delta[w])
            if w != s:
                bc[w] += delta[w]

    return bc
