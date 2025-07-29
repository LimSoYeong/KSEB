import requests
from config.settings import MODEL_SERVER_URL

def chat_with_context(user_text: str) -> str:
    try:
        payload = {"input": user_text}
        response = requests.post(f"{MODEL_SERVER_URL}/invoke", json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("output", "[GPT 응답 없음]")
    except Exception as e:
        return f"[GPT 오류] {str(e)}"
