from langchain_core.runnables import RunnableLambda
from infrastructure.tts_client import text_to_speech

tts_runnable = RunnableLambda(lambda text: text_to_speech(text))
