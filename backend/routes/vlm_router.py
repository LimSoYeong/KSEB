# routes/vlm_router.py

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from infrastructure.vlm_client import describe_image

router = APIRouter(prefix="/vlm", tags=["VLM"])

@router.post("/describe")
async def describe_image_api(image: UploadFile = File(...), prompt: str = Form("이 이미지를 설명해줘")):
    try:
        image_bytes = await image.read()
        result = describe_image(image_bytes, prompt)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))