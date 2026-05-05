import numpy as np


class WaveGlowAdversarialGenerator:
    """WaveGlow 对抗语音生成模拟模块。"""

    def generate(self, source_embedding, target_embedding, level: str = "standard"):
        epsilon_map = {"light": 0.08, "standard": 0.15, "deep": 0.25}
        epsilon = epsilon_map.get(level, 0.15)
        direction = target_embedding - source_embedding
        norm = np.linalg.norm(direction) + 1e-8
        gaussian_noise = np.random.default_rng(7).normal(0, epsilon / 10, size=direction.shape)
        return epsilon * direction / norm + gaussian_noise
