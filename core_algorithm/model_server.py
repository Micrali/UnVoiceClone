from backend.utils.file_handler import copy_as_output
from core_algorithm.modules.speaker_encoder_integration import DynamicSpeakerEncoder
from core_algorithm.modules.kl_divergence_identity_swap import KLIdentitySwapper
from core_algorithm.modules.waveglow_adversarial_generator import WaveGlowAdversarialGenerator
from core_algorithm.modules.pitch_controllable_adjust import PitchController
from core_algorithm.modules.perturbation_optimizer import PerturbationOptimizer


class UnVCModelServer:
    def __init__(self):
        self.encoder = DynamicSpeakerEncoder()
        self.swapper = KLIdentitySwapper()
        self.generator = WaveGlowAdversarialGenerator()
        self.pitch = PitchController()
        self.optimizer = PerturbationOptimizer()

    def process_audio(self, input_path: str, level: str = "standard") -> str:
        embedding = self.encoder.encode(input_path)
        target = self.swapper.select_target(embedding)
        perturbation = self.generator.generate(embedding, target, level=level)
        self.optimizer.optimize(perturbation)
        self.pitch.adjust(input_path)
        return copy_as_output(input_path, suffix=f"unvc_{level}")

    def process_video(self, input_path: str) -> str:
        return copy_as_output(input_path, suffix="unvc_video")
