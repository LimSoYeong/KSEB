from langchain_core.runnables import RunnableLambda
from application.summarize_service import summarize_pipeline

def summarize_runnable_fn(image_bytes: bytes):
    result = summarize_pipeline(image_bytes)
    return {
        "original_text": result.original_text,
        "summary_text": result.summary_text,
        "audio_path": result.audio_path
    }

summarize_runnable = RunnableLambda(summarize_runnable_fn)
