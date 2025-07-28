from langchain_core.runnables import RunnableLambda
from infrastructure.stt_client import speech_to_text

stt_runnable = RunnableLambda(lambda audio_path: speech_to_text(audio_path))
