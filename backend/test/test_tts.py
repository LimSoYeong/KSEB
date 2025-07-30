# test_tts.py
from infrastructure.tts_client import text_to_speech

if __name__ == "__main__":
    text = "안녕하세요. 오늘 하루도 힘내세요!"
    try:
        result_path = text_to_speech(text)
        print("TTS 생성 완료:", result_path)
    except Exception as e:
        print("오류 발생:", e)