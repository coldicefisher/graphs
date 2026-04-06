"""
Main experiment runner that reproduces the paper's results.

Usage:
    python -m research_paper.run_experiments
"""

import numpy as np
import csv
import os

from .datasets import (
    generate_two_moons,
    generate_concentric_circles,
    generate_gaussian_blobs,
)
from .experiment import run_experiment
from .plotting import plot_learning_curves, plot_noise_curves


OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
FIGURES_DIR = os.path.join(OUTPUT_DIR, "figures")

# Experiment parameters matching the paper
N_POINTS = 200
K_NEIGHBORS = 10
BUDGET = 20
N_TRIALS = 20
BASE_SEED = 42

STRATEGIES = ["random", "uncertainty", "max_degree", "betweenness"]
NOISE_RATES = [0.0, 0.05, 0.10, 0.20]

# Dataset configs: generator function, sigma, and kwargs (minus random_state
# which is set per trial)
DATASETS = {
    "Two Moons": {
        "generator": generate_two_moons,
        "sigma": 0.5,
        "gen_kwargs": {"n": N_POINTS, "noise": 0.18},
    },
    "Concentric Circles": {
        "generator": generate_concentric_circles,
        "sigma": 0.8,
        "gen_kwargs": {"n": N_POINTS, "noise": 0.08, "factor": 0.45},
    },
    "Gaussian Blobs": {
        "generator": generate_gaussian_blobs,
        "sigma": 1.0,
        "gen_kwargs": {"n": N_POINTS, "cluster_std": 0.5},
    },
}


def run_strategy_comparison():
    """Run all strategies on all datasets at noise=0 and produce Table 1."""
    print("=" * 60)
    print("STRATEGY COMPARISON (no noise)")
    print("=" * 60)

    os.makedirs(FIGURES_DIR, exist_ok=True)
    summary_rows = []

    for ds_name, ds_config in DATASETS.items():
        print(f"\nDataset: {ds_name}")
        gen = ds_config["generator"]
        gen_kwargs = ds_config["gen_kwargs"]
        sigma = ds_config["sigma"]

        results = {}
        final_accs = {}

        for strategy in STRATEGIES:
            print(f"  Strategy: {strategy}...", end=" ", flush=True)
            mean_acc, std_acc = run_experiment(
                gen, gen_kwargs, strategy,
                budget=BUDGET, k=K_NEIGHBORS, sigma=sigma,
                noise_rate=0.0, n_trials=N_TRIALS, base_seed=BASE_SEED,
            )
            results[strategy] = (mean_acc, std_acc)
            final_accs[strategy] = mean_acc[-1]
            print(f"final acc = {mean_acc[-1]:.4f} "
                  f"(std = {std_acc[-1]:.4f})")

        summary_rows.append({
            "Dataset": ds_name,
            **{s: f"{final_accs[s]:.4f}" for s in STRATEGIES},
        })

        # Plot learning curves
        filename = ds_name.lower().replace(" ", "_") + "_results.png"
        plot_learning_curves(
            results,
            title=f"{ds_name}: Accuracy vs. Queries",
            save_path=os.path.join(FIGURES_DIR, filename),
        )

    # Write summary CSV
    csv_path = os.path.join(OUTPUT_DIR, "strategy_summary.csv")
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Dataset"] + STRATEGIES)
        writer.writeheader()
        writer.writerows(summary_rows)
    print(f"\nSaved: {csv_path}")

    return summary_rows


def run_noise_experiments():
    """Run noise experiments on all datasets and produce noise tables + figures."""
    print("\n" + "=" * 60)
    print("NOISE EXPERIMENTS")
    print("=" * 60)

    os.makedirs(FIGURES_DIR, exist_ok=True)

    for ds_name, ds_config in DATASETS.items():
        print(f"\nDataset: {ds_name}")
        gen = ds_config["generator"]
        gen_kwargs = ds_config["gen_kwargs"]
        sigma = ds_config["sigma"]

        noise_summary_rows = []
        # For each strategy, collect results across noise rates for plotting
        all_noise_results = {s: {} for s in STRATEGIES}

        for noise_rate in NOISE_RATES:
            print(f"\n  Noise rate: {noise_rate:.0%}")
            row = {"Noise Rate": f"{int(noise_rate * 100)}%"}

            for strategy in STRATEGIES:
                print(f"    Strategy: {strategy}...", end=" ", flush=True)
                mean_acc, std_acc = run_experiment(
                    gen, gen_kwargs, strategy,
                    budget=BUDGET, k=K_NEIGHBORS, sigma=sigma,
                    noise_rate=noise_rate, n_trials=N_TRIALS,
                    base_seed=BASE_SEED,
                )
                all_noise_results[strategy][noise_rate] = (mean_acc, std_acc)
                row[strategy] = f"{mean_acc[-1]:.4f}"
                print(f"final acc = {mean_acc[-1]:.4f}")

            noise_summary_rows.append(row)

        # Write noise CSV for this dataset
        csv_name = ds_name.lower().replace(" ", "_") + "_noise_summary.csv"
        csv_path = os.path.join(OUTPUT_DIR, csv_name)
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(
                f, fieldnames=["Noise Rate"] + STRATEGIES)
            writer.writeheader()
            writer.writerows(noise_summary_rows)
        print(f"  Saved: {csv_path}")

        # Plot noise curves for each strategy
        for strategy in STRATEGIES:
            filename = (ds_name.lower().replace(" ", "_")
                        + f"_noise_{strategy}.png")
            plot_noise_curves(
                all_noise_results[strategy],
                strategy_name=strategy,
                title=f"{ds_name}: {strategy} Under Noise",
                save_path=os.path.join(FIGURES_DIR, filename),
            )


def main():
    print("Active Learning for Label Propagation on Graphs")
    print("Reproducing paper experiments...\n")

    run_strategy_comparison()
    run_noise_experiments()

    print("\n" + "=" * 60)
    print("ALL EXPERIMENTS COMPLETE")
    print(f"Results saved to: {OUTPUT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
