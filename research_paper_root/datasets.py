"""
Synthetic dataset generation for active learning experiments.
"""

from sklearn.datasets import make_moons, make_circles, make_blobs


def generate_two_moons(n=200, noise=0.1, random_state=None):
    X, y = make_moons(n_samples=n, noise=noise, random_state=random_state)
    return X, y


def generate_concentric_circles(n=200, noise=0.05, factor=0.5,
                                random_state=None):
    X, y = make_circles(n_samples=n, noise=noise, factor=factor,
                        random_state=random_state)
    return X, y


def generate_gaussian_blobs(n=200, cluster_std=0.5, random_state=None):
    X, y = make_blobs(n_samples=n, centers=2, cluster_std=cluster_std,
                      random_state=random_state)
    return X, y
