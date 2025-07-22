# KSEB backend

# AI 기반 문서 요약 & 음성 챗봇
## 기능
- 이미지 업로드 → vlm + 요약 + TTS 음성
- 음성 업로드 → STT + GPT 응답 + TTS
- WebSocket 실시간 챗

## API 명세서
 사용 API 정리
1. 음성 챗봇
URL: /voice
Method: POST
Request:
Content-Type: multipart/form-data
file: 음성 파일 (mp3 또는 wav)

요청
이름	위치	    타입	       필수 여부	설명
file	FormData	File (mp3/wav)	✅	 사용자 음성 

필드명	         타입	     설명
user_text    	String	     음성 → 텍스트 변환 결과
bot_text	    String	     GPT 응답 텍스트
bot_audio_url	String	   TTS로 생성된 mp3 파일 경로 

Response
json
{
  "user_text": "사용자 음성에서 변환된 텍스트",
  "bot_text": "GPT 응답 텍스트",
  "bot_audio_url": "static/audio/파일명.mp3"
}
 
 2. 이미지 문서 요약
URL: /
Method: POST
Request:
Content-Type: multipart/form-data
file: 이미지 파일 (jpg, png 등)

필드명	         타입	설명
original_text	String	이미지에서 추출된  문서 텍스트
summary_text	String	요약된 텍스트
audio_path	String	    요약된 내용 읽어주는 mp3 파일 



Response
json
{
  "original_text": "이미지에서 추출된 전체 텍스트",
  "summary_text": "요약된 텍스트",
  "audio_path": "static/audio/파일명.mp3"
}

3. WebSocket 텍스트 챗
URL: ws://[서버주소]/ws/chat
Protocol: WebSocket
설명: 텍스트 메시지를 보내면 GPT 응답을 실시간으로 수신

예시
text
[Client] → "안녕 GPT"
[Server] → "'안녕 GPT'에 대한 응답입니다."