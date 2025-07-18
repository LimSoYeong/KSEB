from fastapi import FastAPI
from routes.summarize_router import router as summarize_router
from routes.qa_router import router as qa_router
from routes.chat_ws_router import router as chat_ws_router

app = FastAPI()

# REST API 라우터 등록
app.include_router(summarize_router, prefix="/summarize")
app.include_router(qa_router, prefix="/chat")

# WebSocket 라우터는 직접 선언
app.include_router(chat_ws_router)
