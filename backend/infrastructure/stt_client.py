import requests

def speech_to_text(audio_path: str) -> str:
    url = "https"
    headers = {
        "X-NCP-APIGW-API-KEY-ID": "",
        "X-NCP-APIGW-API-KEY": "",
        "Content-Type": "application/octet-stream"
    }

    with open(audio_path, "rb") as f:
        audio_data = f.read()

    response = requests.post(url + "?lang=Kor", headers=headers, data=audio_data)

    if response.status_code == 200:
        return response.json().get("text", "")
    else:
        print("응답 오류:", response.status_code, response.text)
        return ""