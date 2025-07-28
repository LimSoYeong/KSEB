import os
from dotenv import load_dotenv

load_dotenv()

NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")
TTS_API_URL = os.getenv("TTS_API_URL")
STT_API_URL = os.getenv("STT_API_URL")
MODEL_SERVER_URL = os.getenv("MODEL_SERVER_URL")