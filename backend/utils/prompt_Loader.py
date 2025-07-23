from pathlib import Path

def load_prompt(file_name: str) -> str:
    prompt_path = Path("prompt") / file_name
    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()
