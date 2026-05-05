from flask import Blueprint, jsonify, request

from backend.model_client import ModelClient
from backend.utils.file_handler import save_upload

audio_bp = Blueprint("audio", __name__)
client = ModelClient()


@audio_bp.post("/defend")
def defend_audio():
    file = request.files.get("file")
    level = request.form.get("level", "standard")
    if not file:
        return jsonify({"success": False, "message": "缺少音频文件"}), 400

    input_path = save_upload(file)
    result = client.defend_audio(input_path, level=level)
    return jsonify({"success": True, "message": "音频防御完成", "data": result})
