import numpy as np


class KLIdentitySwapper:
    """基于 KL 散度的匿名异性身份替换策略。"""

    def select_target(self, source_embedding: np.ndarray) -> np.ndarray:
        rng = np.random.default_rng(2026)
        candidates = rng.normal(size=(16, source_embedding.shape[0]))
        source_prob = self._softmax(source_embedding)
        scores = [self._kl_divergence(source_prob, self._softmax(candidate)) for candidate in candidates]
        return candidates[int(np.argmax(scores))]

    @staticmethod
    def _softmax(vector: np.ndarray) -> np.ndarray:
        shifted = vector - np.max(vector)
        exp = np.exp(shifted)
        return exp / np.sum(exp)

    @staticmethod
    def _kl_divergence(p: np.ndarray, q: np.ndarray) -> float:
        eps = 1e-10
        p = np.clip(p, eps, 1.0)
        q = np.clip(q, eps, 1.0)
        return float(np.sum(p * np.log(p / q)))
