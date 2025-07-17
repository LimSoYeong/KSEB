import uuid
from pathlib import Path

def save_temp_file(data: bytes, suffix: str = ".jpg") -> str:
    filename = f"{uuid.uuid4().hex}{suffix}"
    path = Path("static/audio") / filename
    with open(path, "wb") as f:
        f.write(data)
    return str(path)