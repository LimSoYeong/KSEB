from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from services.gpt_service import chat_with_context
from infrastructure.tts_client import text_to_speech
from datetime import datetime

router = APIRouter()

@router.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            #  텍스트 수신
            user_text = await websocket.receive_text()

            # GPT 응답 생성
            bot_response = chat_with_context(user_text)

            # TTS 생성 (오류 발생 시 None 처리)
            try:
                bot_audio_url = text_to_speech(bot_response)
            except Exception as e:
                bot_audio_url = None

            # 응답 JSON으로 프론트에 전송
            await websocket.send_json({
                "bot_text": bot_response,
                "bot_audio_url": bot_audio_url,
                "timestamp": datetime.utcnow().isoformat()
            })
    except WebSocketDisconnect:
        print("WebSocket 연결 종료")
