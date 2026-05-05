import hashlib
import numpy as np


class DynamicSpeakerEncoder:
    """动态集成说话人编码器模拟实现。"""

    def __init__(self):
        self.encoders = ["ECAPA-TDNN", "GE2E", "d-vector", "StyleEncoder"]
        self.weights = np.array([0.35, 0.25, 0.2, 0.2])

    def encode(self, audio_path: str) -> np.ndarray:
        seed = int(hashlib.md5(audio_path.encode("utf-8")).hexdigest()[:8], 16)
        rng = np.random.default_rng(seed)
        embeddings = rng.normal(size=(len(self.encoders), 256))
        return (embeddings * self.weights[:, None]).sum(axis=0)
