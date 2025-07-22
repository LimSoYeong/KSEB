import uuid
from pathlib import Path
import requests
from config.settings import TTS_API_KEY

def text_to_speech(text: str) -> str:
    url = "https"
    headers = {
        "X-NCP-APIGW-API-KEY-ID": "client-id",
        "X-NCP-APIGW-API-KEY": TTS_API_KEY,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "speaker": "nara",
        "text": text,
        "format": "mp3"
    }

    response = requests.post(url, headers=headers, data=data)
    filename = f"{uuid.uuid4().hex}.mp3"
    path = Path("static/audio") / filename
    with open(path, "wb") as f:
        f.write(response.content)
    return str(path)
