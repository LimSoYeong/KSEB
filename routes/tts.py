from flask import Blueprint, request, jsonify, send_file
from services.tts_engine import text_to_speech

tts_bp = Blueprint('tts', __name__)

@tts_bp.route('/tts', methods=['POST'])
def tts_route():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "텍스트 없음."}), 400

    try:
        audio_path = text_to_speech(text)
        return send_file(audio_path, mimetype="audio/mpeg")
    except Exception as e:
        return jsonify({"error": str(e)}), 500
