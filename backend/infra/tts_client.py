import uuid
from pathlib import Path
import requests
from config.settings import TTS_API_KEY

def text_to_speech(text: str) -> str:
    filename = f"{uuid.uuid4().hex}.mp3"
    path = Path("static/audio") / filename
    with open(path, "wb") as f:
        f.write(b"DUMMY MP3 DATA")  
        # TODO: TTS API, 현재는 더미
    return str(path)
