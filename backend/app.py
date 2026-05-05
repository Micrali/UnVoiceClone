from flask import Flask, jsonify
try:
    from flask_cors import CORS
except ImportError:
    def CORS(app):
        return app

try:
    from api.auth_api import auth_bp
    from api.audio_defend_api import audio_bp
    from api.video_defend_api import video_bp
    from api.test_api import test_bp
    from api.system_api import system_bp
except ImportError:
    from backend.api.auth_api import auth_bp
    from backend.api.audio_defend_api import audio_bp
    from backend.api.video_defend_api import video_bp
    from backend.api.test_api import test_bp
    from backend.api.system_api import system_bp


def create_app():
    app = Flask(__name__)
    try:
        app.config.from_object("config.app_config.AppConfig")
    except Exception:
        app.config.from_object("backend.config.app_config.AppConfig")
    CORS(app)

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(audio_bp, url_prefix="/api/audio")
    app.register_blueprint(video_bp, url_prefix="/api/video")
    app.register_blueprint(test_bp, url_prefix="/api/test")
    app.register_blueprint(system_bp, url_prefix="/api/system")

    @app.get("/api/health")
    def health():
        return jsonify({"status": "ok", "service": "UnVoiceClone API", "version": "1.0.0"})

    @app.get("/api/docs")
    def docs():
        return jsonify({
            "health": "GET /api/health",
            "login": "POST /api/auth/login",
            "audio_defend": "POST /api/audio/defend",
            "video_defend": "POST /api/video/defend",
            "test_convert": "POST /api/test/convert",
            "system_stats": "GET /api/system/stats",
        })

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000, debug=True)
