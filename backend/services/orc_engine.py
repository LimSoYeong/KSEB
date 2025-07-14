# paddle모델 쓸 경우 코드
from paddleocr import PaddleOCR
import tempfile
from PIL import Image

# OCR 초기화
ocr_model = PaddleOCR(use_angle_cls=True, lang='korean')  # 설치 필요: pip install paddleocr paddlepaddle

def extract_text_from_image(image_file):
    """
    이미지 파일에서 텍스트 추출 (PaddleOCR 사용)
    """
    try:
        # Flask의 FileStorage 객체 -> 임시 저장
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp:
            image_file.save(tmp.name)
            result = ocr_model.ocr(tmp.name, cls=True)

        # 추출된 텍스트를 한 줄로 정리
        extracted_text = "\n".join([line[1][0] for line in result[0]])
        return extracted_text

    except Exception as e:
        print(f"[OCR 오류] {e}")
        return ""
