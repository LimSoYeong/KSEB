import os
from dotenv import load_dotenv

load_dotenv()

CLOVA_OCR_SECRET = os.getenv("CLOVA_OCR_SECRET")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TTS_API_KEY = os.getenv("TTS_API_KEY")
OPEN_API_URL = os.getenv("OPEN_API_URL")

## 모든 API를 가져온다는 가정하에 API를 따로 관리(보안)
## 학습좋은 모델있으면 API뺴고 routes,services,db에서 수정