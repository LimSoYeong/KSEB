from infrastructure.vlm_client import extract_text_from_image
from infrastructure.tts_client import text_to_speech
from domain.summarize_entity import SummaryResult

def summarize_pipeline(image_bytes: bytes) -> SummaryResult:
    extracted_text = extract_text_from_image(image_bytes)
    summary_text = extracted_text[:100] + "..." if len(extracted_text) > 100 else extracted_text
    audio_path = text_to_speech(summary_text)

    return SummaryResult(extracted_text, summary_text, audio_path)
