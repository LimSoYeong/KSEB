from utils.file_utils import save_temp_file
from infrastructure.stt_client import speech_to_text
from services.gpt_service import chat_with_context
from infrastructure.tts_client import text_to_speech

def chat_from_voice(audio_bytes: bytes) -> dict:
    audio_path = save_temp_file(audio_bytes, suffix=".mp3")

    user_text = speech_to_text(audio_path)
    bot_text = chat_with_context(user_text)
    bot_audio = text_to_speech(bot_text)

    return {
        "user_text": user_text,
        "bot_text": bot_text,
        "bot_audio_url": bot_audio
    }
