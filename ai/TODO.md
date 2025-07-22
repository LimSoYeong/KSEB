## TODO - ai

### Qwen

#### 1. 학습 전 Qwen 과 LoRA 학습 후 Qwen 비교

- 학습 전 Qwen 결과 확인
[] 추론 속도 줄이기
[*] Vision Encoder 분리 캐싱 ->  이미지 임베딩 캐시처리로 다른 프롬프트에 재사용할 수 있도록
[] batch 추론 처리 구현 : 여러 이미지 prompt 묶어서 한 번에 추론