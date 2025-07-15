from flask import Blueprint, request
from services.audio_service import process_audio

audio_bp = Blueprint('audio', __name__)

@audio_bp.route("/process", methods=["POST"])
def handle_process():
    return process_audio(request)
