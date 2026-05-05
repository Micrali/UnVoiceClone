from flask import Blueprint, jsonify, request

from backend.model_client import ModelClient
from backend.utils.file_handler import save_upload

video_bp = Blueprint("video", __name__)
client = ModelClient()


@video_bp.post("/defend")
def defend_video():
    file = request.files.get("file")
    if not file:
        return jsonify({"success": False, "message": "缺少视频文件"}), 400

    input_path = save_upload(file)
    result = client.defend_video(input_path)
    return jsonify({"success": True, "message": "视频防御完成", "data": result})
