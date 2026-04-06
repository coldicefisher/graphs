"""
Active learning experiment runner.

Runs the active learning loop: at each iteration, compute GFHF, evaluate
accuracy, select next node via strategy, query its (possibly noisy) label,
and repeat until the budget is exhausted.
"""

import numpy as np
from .gfhf import build_weight_matrix, knn_sparsify, gfhf_closed_form
from .strategies import (
    random_selection,
    uncertainty_sampling,
    max_degree_selection,
    betweenness_centrality_selection,
)
from .noise import flip_label


STRATEGIES = {
    "random": "random",
    "uncertainty": "uncertainty",
    "max_degree": "max_degree",
    "betweenness": "betweenness",
}


def run_single_trial(X, y_true, strategy_name, budget=20, k=10, sigma=1.0,
                     noise_rate=0.0, seed=None):
    """Run one active learning trial.

    Returns an array of accuracies of length (budget + 1), where index 0 is
    the accuracy after the initial two seed labels and index B is the accuracy
    after all B queries.
    """
    rng = np.random.default_rng(seed)
    n = len(y_true)

    # Build and sparsify weight matrix
    W = build_weight_matrix(X, sigma=sigma)
    W = knn_sparsify(W, k=k)

    # Initialize: one random node per class as seed labels
    class0 = np.where(y_true == 0)[0]
    class1 = np.where(y_true == 1)[0]
    seed0 = rng.choice(class0)
    seed1 = rng.choice(class1)

    labeled_indices = [seed0, seed1]
    labels = np.array([y_true[seed0], y_true[seed1]])

    accuracies = []

    for t in range(budget + 1):
        # Compute GFHF predictions
        f = gfhf_closed_form(W, np.array(labeled_indices), labels)

        # Evaluate accuracy on unlabeled nodes
        labeled_set = set(labeled_indices)
        unlabeled = np.array([i for i in range(n) if i not in labeled_set])

        if len(unlabeled) == 0:
            accuracies.append(1.0)
            continue

        predictions = (f[unlabeled] >= 0.5).astype(int)
        accuracy = np.mean(predictions == y_true[unlabeled])
        accuracies.append(accuracy)

        if t == budget:
            break

        # Select next node to query
        if strategy_name == "random":
            selected = random_selection(f, unlabeled, rng)
        elif strategy_name == "uncertainty":
            selected = uncertainty_sampling(f, unlabeled, rng)
        elif strategy_name == "max_degree":
            selected = max_degree_selection(W, unlabeled, rng)
        elif strategy_name == "betweenness":
            selected = betweenness_centrality_selection(W, unlabeled, rng)
        else:
            raise ValueError(f"Unknown strategy: {strategy_name}")

        # Query label (possibly noisy)
        queried_label = flip_label(y_true[selected], noise_rate, rng)

        # Add to labeled set
        labeled_indices.append(selected)
        labels = np.append(labels, queried_label)

    return np.array(accuracies)


def run_experiment(dataset_generator, gen_kwargs, strategy_name, budget=20,
                   k=10, sigma=1.0, noise_rate=0.0, n_trials=20,
                   base_seed=42):
    """Run multiple trials with fresh data per trial and return mean/std accuracies."""
    all_accuracies = []
    for trial in range(n_trials):
        seed = base_seed + trial
        # Generate fresh data each trial for realistic variance
        kwargs = {**gen_kwargs, "random_state": seed}
        X, y_true = dataset_generator(**kwargs)
        acc = run_single_trial(
            X, y_true, strategy_name,
            budget=budget, k=k, sigma=sigma,
            noise_rate=noise_rate, seed=seed,
        )
        all_accuracies.append(acc)
    return np.mean(all_accuracies, axis=0), np.std(all_accuracies, axis=0)
