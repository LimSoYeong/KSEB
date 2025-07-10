from flask import Blueprint, request, jsonify
from services.stt_engine import transcribe_audio

stt_bp = Blueprint('stt', __name__)

@stt_bp.route('/stt', methods=['POST'])
def stt_route():
    if 'audio' not in request.files:
        return jsonify({"error": "오디오 없음."}), 400

    audio = request.files['audio']
    try:
        text = transcribe_audio(audio)
        return jsonify({"text": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
