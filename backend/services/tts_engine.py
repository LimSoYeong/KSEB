import requests
import uuid
import os

def text_to_speech(text):
    # 추후 TTS 엔진(Google, Naver 등) 연동 예정
    # 현재는 더미 mp3 경로 반환
    dummy_audio_path = "static/audio/dummy.mp3"
    return dummy_audio_path

# 환경변수나 config 파일에서 불러오도록 설정 가능
NAVER_CLOVA_CLIENT_ID = ""
NAVER_CLOVA_CLIENT_SECRET = ""
