from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from services.gpt_service import chat_with_context

router = APIRouter()

@router.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            user_text = await websocket.receive_text()
            bot_response = chat_with_context(user_text)
            await websocket.send_text(bot_response)
    except WebSocketDisconnect:
        print("WebSocket 연결 종료")
