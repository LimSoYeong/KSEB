from fastapi import APIRouter, UploadFile, File
from application.summarize_service import summarize_pipeline

router = APIRouter()

@router.post("/")
async def summarize(file: UploadFile = File(...)):
    image_bytes = await file.read()
    result = summarize_pipeline(image_bytes)

    return {
        "original_text": result.original_text,
        "summary_text": result.summary_text,
        "audio_path": result.audio_path
    }
