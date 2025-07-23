import uuid
from pathlib import Path
import requests
from config.settings import TTS_API_KEY

def text_to_speech(text: str) -> str:
    filename = f"{uuid.uuid4().hex}.mp3"
    path = Path("static/audio") / filename

    url = ""
    headers = {
        "X-NCP-APIGW-API-KEY-ID": os.getenv("NAVER_CLIENT_ID"),
        "X-NCP-APIGW-API-KEY": TTS_API_KEY,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "speaker": "nara",
        "speed": "0",
        "text": text
    }

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        with open(path, "wb") as f:
            f.write(response.content)
        return str(path)
    else:
        raise RuntimeError(f"TTS 요청 실패: {response.status_code} - {response.text}")
