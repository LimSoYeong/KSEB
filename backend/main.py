from fastapi import FastAPI
from presentation.summarize_router import router as summarize_router

app = FastAPI()
app.include_router(summarize_router, prefix="/summarize")
