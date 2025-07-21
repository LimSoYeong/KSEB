import uuid
from pathlib import Path

def text_to_speech(text: str) -> str:
    filename = f"{uuid.uuid4().hex}.mp3"
    path = Path("static/audio") / filename
    with open(path, "wb") as f:
        f.write(b"DUMMY MP3 DATA")  
        # TODO: TTS API로 대체
    return str(path)
