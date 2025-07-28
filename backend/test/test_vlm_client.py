import os
import pytest
from infrastructure.vlm_client import extract_text_from_image

@pytest.fixture
def image_bytes():
    image_path = "/root/2025-siseon-eum/ai/data/img/img_001.jpg"
    with open(image_path, "rb") as f:
        return f.read()

def test_extract_text_from_image(image_bytes):
    output = extract_text_from_image(image_bytes)
    print(f"추출된 텍스트: {output}")
    assert isinstance(output, str)
    assert len(output) > 0