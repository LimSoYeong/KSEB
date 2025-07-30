import uuid
from pathlib import Path
import requests
import os
from config.settings import NAVER_TTS_CLIENT_ID, NAVER_TTS_CLIENT_SECRET

TTS_URL = "https://naveropenapi.apigw.ntruss.com/tts-premium/v1/tts"

def text_to_speech(text: str) -> str:
    filename = f"{uuid.uuid4().hex}.mp3"
    path = Path("static/audio") / filename
    try:
        path.parent.mkdir(parents=True, exist_ok=True) # 폴더 없을 경우 생성
    except FileExistsError:
        pass

    headers = {
        "x-ncp-apigw-api-key-id": NAVER_TTS_CLIENT_ID,
        "x-ncp-apigw-api-key": NAVER_TTS_CLIENT_SECRET,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "speaker": "nara",
        "speed": "0",
        "text": text,
        "format" : "mp3", # 파일 포맷 설정
    }

    response = requests.post(TTS_URL, headers=headers, data=data)
    if response.status_code == 200:
        with open(path, "wb") as f:
            f.write(response.content)
        return f"/static/audio/{filename}" # 클라이언트용 경로
    else:
        raise RuntimeError(f"TTS 요청 실패: {response.status_code} - {response.text}")
