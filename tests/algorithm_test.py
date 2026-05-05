import numpy as np
from core_algorithm.modules.kl_divergence_identity_swap import KLIdentitySwapper


def test_identity_swap_shape():
    source = np.ones(256)
    target = KLIdentitySwapper().select_target(source)
    assert target.shape == source.shape
