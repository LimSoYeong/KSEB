from model import model, processor
from PIL import Image
import io
import torch
import time

def run_inference(image_bytes: bytes, prompt: str = "이 이미지를 노인을 위해 쉽게 설명해줘") -> dict:
    # 이미지 로딩
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    # prompt 메시지 구조 생성
    messages = [
        {"role": "user", "content": [
            {"type": "image", "image": image},
            {"type": "text", "text": prompt}
        ]}
    ]
    text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

    inputs = processor(
        text=[text],
        images=[image],
        return_tensors="pt"
    ).to(model.device)

    with torch.no_grad():
        start = time.time()
        generated_ids = model.generate(
            **inputs,
            max_new_tokens=256,
            do_sample=False
        )
        end = time.time()

    generated_ids_trimmed = [
        out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    output_text = processor.batch_decode(
        generated_ids_trimmed,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=False
    )[0]

    return {
        "output": output_text,
        "inference_time": round(end - start, 2)
    }