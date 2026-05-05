import numpy as np


class PerturbationOptimizer:
    """梯度正则化与 SAM 扰动优化模拟模块。"""

    def optimize(self, perturbation):
        clipped = np.clip(perturbation, -0.3, 0.3)
        return clipped / (np.linalg.norm(clipped) + 1e-8)
