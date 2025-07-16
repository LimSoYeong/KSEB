from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
import tempfile, uuid
import openai
import base64
import os
import uvicorn
from io import BytesIO

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# from services.stt import sst API
# from services.tts import tts API
# from services.vlm import vlm 모델(?)

@app.post("/process")
async def process(image: UploadFile = File(...), audio: UploadFile = File(...)):
    # 1. 업로드 받은 파일 저장
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_image:
        tmp_image.write(await image.read())

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_audio:
        tmp_audio.write(await audio.read())

    # 2. STT
    text = clova_stt(tmp_audio.name)

    # 3. VLM 질문 응답
    answer = vlm_ask(image_path=tmp_image.name, question=text)

    # 4. TTS 변환
    mp3_data = clova_tts(answer)  # 반환

    # 5. mp3 파일을 클라이언트에게 들려준다.
    return StreamingResponse(BytesIO(mp3_data), media_type="audio/mpeg")

