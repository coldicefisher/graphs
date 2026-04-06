"""
Plotting utilities for active learning experiments.
"""

import matplotlib.pyplot as plt
import numpy as np
import os


def plot_learning_curves(results, title, save_path=None):
    """Plot accuracy vs. number of queries for multiple strategies.

    results: dict of {strategy_name: (mean_accuracies, std_accuracies)}
    """
    fig, ax = plt.subplots(figsize=(8, 5))

    for name, (mean_acc, std_acc) in results.items():
        x = np.arange(len(mean_acc))
        ax.plot(x, mean_acc, marker="o", markersize=4, label=name)
        ax.fill_between(x, mean_acc - std_acc, mean_acc + std_acc, alpha=0.15)

    ax.set_xlabel("Number of Queries")
    ax.set_ylabel("Accuracy on Unlabeled Nodes")
    ax.set_title(title)
    ax.legend()
    ax.grid(True, alpha=0.3)

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
        print(f"Saved: {save_path}")
    plt.close(fig)


def plot_noise_curves(noise_results, strategy_name, title, save_path=None):
    """Plot accuracy vs. queries for one strategy under different noise rates.

    noise_results: dict of {noise_rate: (mean_accuracies, std_accuracies)}
    """
    fig, ax = plt.subplots(figsize=(8, 5))

    for noise_rate, (mean_acc, std_acc) in sorted(noise_results.items()):
        x = np.arange(len(mean_acc))
        label = f"noise={int(noise_rate * 100)}%"
        ax.plot(x, mean_acc, marker="o", markersize=4, label=label)
        ax.fill_between(x, mean_acc - std_acc, mean_acc + std_acc, alpha=0.15)

    ax.set_xlabel("Number of Queries")
    ax.set_ylabel("Accuracy on Unlabeled Nodes")
    ax.set_title(title)
    ax.legend()
    ax.grid(True, alpha=0.3)

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
        print(f"Saved: {save_path}")
    plt.close(fig)
