from flask import Blueprint, jsonify

system_bp = Blueprint("system", __name__)


@system_bp.get("/stats")
def stats():
    return jsonify({
        "success": True,
        "data": {
            "total_files": 12860,
            "today_files": 236,
            "avg_success_rate": 66.29,
            "avg_similarity": 84.73,
            "avg_duration": 7.8,
            "availability": 99.98,
            "risk_blocks": 9321,
            "cpu": 42,
            "memory": 58,
            "gpu": 36,
            "records": [
                {"name": "sample_voice.wav", "type": "音频", "duration": "5.2s", "time": "2026-05-05 09:30"},
                {"name": "interview.mp4", "type": "视频", "duration": "18.6s", "time": "2026-05-05 10:10"},
            ],
        },
    })
