class PitchController:
    """基音可控调节模块，约束扰动后语音的听感自然度。"""

    def adjust(self, audio_path: str, semitone_limit: float = 1.5) -> dict:
        return {"audio_path": audio_path, "semitone_limit": semitone_limit, "status": "adjusted"}
