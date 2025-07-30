from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from langserve import add_routes
from runnables.summarize_runnable import summarize_runnable
from runnables.chat_runnable import chat_runnable
from runnables.tts_runnable import tts_runnable
from runnables.stt_runnable import stt_runnable
from routes import summarize, qa_router, chat_ws_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 정적 파일 (mp3 저장된 audio 경로 포함)
app.mount("/static", StaticFiles(directory="static"), name="static")

# LangServe API 등록 
add_routes(app, summarize_runnable, path="/lang/summarize")
add_routes(app, chat_runnable, path="/lang/chat")
add_routes(app, tts_runnable, path="/lang/tts")
add_routes(app, stt_runnable, path="/lang/stt")

# 일반 REST + WebSocket 라우터 등록
app.include_router(summarize.router, prefix="/summarize")
app.include_router(qa_router.router, prefix="/qa")
app.include_router(chat_ws_router.router)
