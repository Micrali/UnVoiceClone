from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
UPLOAD_DIR = ROOT_DIR / "runtime" / "uploads"
OUTPUT_DIR = ROOT_DIR / "runtime" / "outputs"
MODEL_DIR = ROOT_DIR / "models" / "pretrained"
STATIC_FRONTEND_DIR = ROOT_DIR / "frontend" / "web_static"

for path in (UPLOAD_DIR, OUTPUT_DIR, MODEL_DIR):
    path.mkdir(parents=True, exist_ok=True)
