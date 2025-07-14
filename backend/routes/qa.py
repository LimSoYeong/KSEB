from fastapi import APIRouter, UploadFile
from services import stt_engine, gpt_service, tts_engine

router = APIRouter()

@router.post("/qa/audio")
async def question_from_audio(audio_file: UploadFile):
    # 1. STT: 음성 → 텍스트
    question_text = stt_engine.speech_to_text(audio_file.file)

    # 2. context(OCR)
    context = get_context_data()  # 예시 

    # 3. 질문응답용 프롬프트 구성 및 호출
    answer_text = gpt_service.answer_question(context=context, question=question_text)

    # 4. TTS
    audio_path = tts_engine.text_to_speech(answer_text)

    # 5. 오디오 파일 경로 리턴 함수
    return {"audio_url": audio_path, "answer": answer_text}
