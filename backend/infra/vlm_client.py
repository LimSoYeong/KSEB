from transformers import DonutProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch, io
from infrastructure.prompt_loader import load_prompt

processor = DonutProcessor.from_pretrained("")
model = VisionEncoderDecoderModel.from_pretrained("")
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

prompt = load_prompt("summary")

def extract_text_from_image(image_bytes: bytes) -> str:
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    prompt = "<s_docvqa><s_question>이 문서 내용을 요약해줘</s_question><s_answer>"
    inputs = processor(image, prompt, return_tensors="pt").to(device)
    output = model.generate(**inputs, max_length=512)
    answer = processor.batch_decode(output, skip_special_tokens=True)[0]
    return answer.replace(prompt, "").strip()
