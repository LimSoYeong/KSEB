from transformers import Qwen2_5_VLForConditionalGeneration, AutoProcessor
from qwen_vl_utils import process_vision_info
from PIL import Image
from pathlib import Path
import torch
import time

total_time = 0 # 시간 계산용
base_dir = Path(__file__).resolve().parent.parent # 현재 파일 기준으로 경로 설정 : KSEB/ai

# ====== 설정 ======
# 1️⃣ 이미지 경로 (사용 안 할 땐 None)
# image_path = base_dir / "data" / "img" / "img_001.jpg"
image_path = None

# 2️⃣ 캐시된 임베딩 경로 (사용 안 할 땐 None)
embedding_path = base_dir / "qwen" / "cached_embeds" / "img_001.pt"

prompt_text = "이 문서를 노인을 위해 쉽게 설명해줘"


# 모델 로드
model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2.5-VL-7B-Instruct", 
    torch_dtype=torch.float16, # rtx 4060 에서 메모리/속도에 효율적
    device_map="auto"
)
model.eval()  # 평가 모드 전환 : 추론시에 일관성 유지하기 위함
print(f"모델 디바이스: {model.device if hasattr(model, 'device') else '멀티 디바이스'}")

# 조건에 따라 processor 초기화
if image_path and image_path.exists():
    # 이미지 크기 조절이 필요한 경우
    min_pixels = 256 * 14 * 14
    max_pixels = 1280 * 14 * 14
    processor = AutoProcessor.from_pretrained(
        "Qwen/Qwen2.5-VL-7B-Instruct",
        min_pixels=min_pixels,
        max_pixels=max_pixels
    )
else:
    # 임베딩 사용할 경우 크기 조절 필요 없음
    processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-VL-7B-Instruct")

# ====== 메시지 준비 ======
if image_path and image_path.exists():
    image = Image.open(image_path).convert("RGB")
    messages = [
        {"role": "user", "content": [
            {"type": "image", "image": image},
            {"type": "text", "text": prompt_text}
        ]}
    ]
    image_inputs, video_inputs = process_vision_info(messages)
elif embedding_path and embedding_path.exists():
    # 캐시된 임베딩 불러오기
    image_inputs = torch.load(embedding_path, weights_only=False)
    video_inputs = None
    messages = [
        {"role": "user", "content": [
            {"type": "image", "image": "<cached>"},
            {"type": "text", "text": prompt_text}
        ]}
    ]
else:
    raise FileNotFoundError("이미지나 임베딩 파일 중 하나는 반드시 필요합니다.")

# ====== 입력 생성 ======
text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

inputs = processor(
    text=[text],
    images=image_inputs,
    videos=video_inputs,
    padding=True,
    return_tensors="pt",
)
inputs = inputs.to(model.device)

# ====== 추론 ======
start = time.time()
with torch.no_grad(): # no_grad : 추론시에만 사용. gradient를 계산하지 않는다는 뜻
    generated_ids = model.generate(
        **inputs,
        max_new_tokens=256, # 혹은 128
        do_sample=False # 샘플링을 하지 않고, greedy 방식으로 출력 생성
    )
    generated_ids_trimmed = [
        out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    output_text = processor.batch_decode(
        generated_ids_trimmed,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=False
    )
end = time.time()

# ====== 결과 출력 ======
print(f"🕒 처리 시간: {end - start:.2f}초")
print("🧠 모델 응답:\n", output_text[0])