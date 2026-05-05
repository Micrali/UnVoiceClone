import numpy as np


def embedding_loss(source, defended):
    source = np.asarray(source)
    defended = np.asarray(defended)
    cosine = np.dot(source, defended) / ((np.linalg.norm(source) * np.linalg.norm(defended)) + 1e-8)
    return 1.0 - cosine
