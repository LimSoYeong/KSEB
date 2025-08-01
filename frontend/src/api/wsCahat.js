// src/api/wsChat.js
export function connectChatWebSocket(onMessage) {
  // ws:// (로컬, 배포에 따라 다름)
  const socket = new WebSocket('ws://localhost:8000/ws/chat');
  socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    onMessage(data); // { bot_text, bot_audio_url, timestamp }
  };
  return socket;
}
