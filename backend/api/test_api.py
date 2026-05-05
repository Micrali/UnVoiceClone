from flask import Blueprint, jsonify, request

from backend.model_client import ModelClient

test_bp = Blueprint("test", __name__)
client = ModelClient()


@test_bp.post("/convert")
def convert_test():
    return jsonify({"success": True, "data": client.run_clone_test("voice_conversion")})


@test_bp.post("/synthesis")
def synthesis_test():
    payload = request.get_json(silent=True) or {}
    result = client.run_clone_test("tts_synthesis")
    result["text"] = payload.get("text", "用声无恙守护声纹隐私。")
    return jsonify({"success": True, "data": result})
