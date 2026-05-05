import os


class ModelLoader:
    def __init__(self, model_dir="models/pretrained"):
        self.model_dir = model_dir

    def list_models(self):
        if not os.path.exists(self.model_dir):
            return []
        return [name for name in os.listdir(self.model_dir) if not name.startswith(".")]

    def load(self, name: str):
        return {"name": name, "path": os.path.join(self.model_dir, name), "loaded": True}
