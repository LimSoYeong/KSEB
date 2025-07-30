from infrastructure.stt_client import speech_to_text

if __name__ == "__main__":
    audio_file = "static/audio/sample.mp3"  # 테스트용 오디오 파일 경로
    try:
        text = speech_to_text(audio_file)
        print("변환된 텍스트:", text)
    except Exception as e:
        print("오류 발생:", e)