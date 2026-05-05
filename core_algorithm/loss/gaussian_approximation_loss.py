import numpy as np


def gaussian_approximation_loss(perturbation, sigma=0.15):
    perturbation = np.asarray(perturbation)
    variance = np.var(perturbation) + 1e-8
    return float((variance - sigma ** 2) ** 2)
