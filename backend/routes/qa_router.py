from fastapi import APIRouter, UploadFile, File
from application.chat_service import chat_from_voice

router = APIRouter()

@router.post("/voice")
async def voice_chat(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    result = chat_from_voice(audio_bytes)
    return result
