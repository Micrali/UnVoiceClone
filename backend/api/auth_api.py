from flask import Blueprint, jsonify, request

auth_bp = Blueprint("auth", __name__)


@auth_bp.post("/login")
def login():
    data = request.get_json(silent=True) or {}
    if data.get("username") == "admin" and data.get("password") == "admin123":
        return jsonify({"success": True, "token": "unvc-demo-token", "user": {"name": "admin", "role": "管理员"}})
    return jsonify({"success": False, "message": "用户名或密码错误"}), 401


@auth_bp.get("/profile")
def profile():
    return jsonify({"name": "admin", "role": "管理员", "team": "用声无恙"})
