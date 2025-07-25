from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes import summarize, qa_router, chat_ws_router
from langserve import add_routes
from runnables.summarize_runnable import summarize_runnable
from runnables.chat_runnable import chat_runnable
from runnables.tts_runnable import tts_runnable
from runnables.stt_runnable import stt_runnable

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(summarize.router, prefix="/summarize")
app.include_router(qa_router.router, prefix="/qa")
app.include_router(chat_ws_router.router)

add_routes(app, summarize_runnable, path="/lang/summarize")
add_routes(app, chat_runnable, path="/lang/chat")
add_routes(app, tts_runnable, path="/lang/tts")
add_routes(app, stt_runnable, path="/lang/stt")
