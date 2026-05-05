import numpy as np


def soft_constraint_loss(signal, reference, alpha=0.2):
    return alpha * float(np.mean((np.asarray(signal) - np.asarray(reference)) ** 2))
