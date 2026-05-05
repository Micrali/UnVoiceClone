from pathlib import Path
import yaml

ROOT_DIR = Path(__file__).resolve().parents[2]
PARAMS_PATH = ROOT_DIR / "configs" / "algorithm_params.yaml"


def load_algorithm_params():
    with open(PARAMS_PATH, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)
