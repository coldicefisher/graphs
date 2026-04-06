"""
GFHF (Gaussian Fields and Harmonic Functions) implementation.

Implements the label propagation method from Zhu, Ghahramani, and Lafferty (2003).
"""

import numpy as np


def build_weight_matrix(X, sigma=1.0):
    """Construct a full Gaussian kernel weight matrix.

    W_ij = exp(-||x_i - x_j||^2 / (2 * sigma^2))
    """
    n = X.shape[0]
    sq_norms = np.sum(X ** 2, axis=1)
    dist_sq = sq_norms[:, None] + sq_norms[None, :] - 2.0 * X @ X.T
    dist_sq = np.maximum(dist_sq, 0.0)  # numerical safety
    W = np.exp(-dist_sq / (2.0 * sigma ** 2))
    np.fill_diagonal(W, 0.0)
    return W


def knn_sparsify(W, k=10):
    """Sparsify weight matrix to k-nearest neighbors, then symmetrize."""
    n = W.shape[0]
    W_sparse = np.zeros_like(W)
    for i in range(n):
        neighbors = np.argsort(W[i])[::-1][:k]
        W_sparse[i, neighbors] = W[i, neighbors]
    # Symmetrize: keep the max of W_sparse[i,j] and W_sparse[j,i]
    W_sparse = np.maximum(W_sparse, W_sparse.T)
    return W_sparse


def gfhf_closed_form(W, labeled_indices, labels):
    """Compute the GFHF harmonic function via closed-form solution.

    f_u = (D_uu - W_uu)^{-1} W_ul f_l

    Returns the full prediction vector f of length n.
    """
    n = W.shape[0]
    all_indices = np.arange(n)
    labeled_set = set(labeled_indices)
    unlabeled_indices = np.array(
        [i for i in all_indices if i not in labeled_set])

    if len(unlabeled_indices) == 0:
        f = np.zeros(n)
        f[labeled_indices] = labels.astype(float)
        return f

    W_uu = W[np.ix_(unlabeled_indices, unlabeled_indices)]
    W_ul = W[np.ix_(unlabeled_indices, labeled_indices)]
    D_uu = np.diag(np.sum(W[unlabeled_indices, :], axis=1))

    A = D_uu - W_uu
    b = W_ul @ labels.astype(float)
    try:
        f_u = np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        # Regularize if singular (disconnected components)
        A += 1e-10 * np.eye(len(A))
        f_u = np.linalg.solve(A, b)

    f = np.zeros(n)
    f[labeled_indices] = labels.astype(float)
    f[unlabeled_indices] = f_u
    return f
