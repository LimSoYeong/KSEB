import requests
from config.settings import STT_API_KEY

def speech_to_text(audio_path: str) -> str:
    url = ""
    headers = {
        "X-NCP-APIGW-API-KEY-ID": os.getenv("NAVER_CLIENT_ID"),
        "X-NCP-APIGW-API-KEY": STT_API_KEY,
        "Content-Type": "application/octet-stream"
    }
    with open(audio_path, "rb") as f:
        audio_data = f.read()

    response = requests.post(url, headers=headers, data=audio_data)
    if response.status_code == 200:
        return response.json().get("text", "")
    else:
        raise RuntimeError(f"STT 오류: {response.status_code} - {response.text}")

