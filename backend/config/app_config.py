from pathlib import Path
import yaml

ROOT_DIR = Path(__file__).resolve().parents[2]
CONFIG_PATH = ROOT_DIR / "configs" / "server_config.yaml"


def load_server_config():
    if not CONFIG_PATH.exists():
        return {
            "server": {
                "backend_host": "127.0.0.1",
                "backend_port": 5000,
                "frontend_host": "127.0.0.1",
                "frontend_port": 8080,
                "upload_limit_mb": 500,
            }
        }
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


_server = load_server_config().get("server", {})


class AppConfig:
    SECRET_KEY = "unvc-dev-secret-key"
    JSON_AS_ASCII = False
    MAX_CONTENT_LENGTH = int(_server.get("upload_limit_mb", 500)) * 1024 * 1024
