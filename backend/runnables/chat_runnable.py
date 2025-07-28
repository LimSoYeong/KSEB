from langchain_core.runnables import RunnableLambda
from services.gpt_service import chat_with_context

chat_runnable = RunnableLambda(lambda text: chat_with_context(text))
