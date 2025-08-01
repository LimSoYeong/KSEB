// src/api/stt.js
export async function sttQnA(file) {
  const formData = new FormData();
  formData.append('file', file);

  const res = await fetch('http://localhost:8000/stt', {
    method: 'POST',
    body: formData,
  });
  if (!res.ok) throw new Error('음성 질문 실패');
  return await res.json(); // { user_text, bot_text, bot_audio_url }
}
