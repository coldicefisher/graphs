"""
Symmetric label-flipping noise model.
"""

import numpy as np


def flip_label(true_label, noise_rate, rng):
    """Return the (possibly flipped) label under symmetric noise.

    With probability (1 - noise_rate), return the true label.
    With probability noise_rate, return 1 - true_label.
    """
    if rng.random() < noise_rate:
        return 1 - true_label
    return true_label
