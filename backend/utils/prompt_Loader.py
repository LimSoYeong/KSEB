from pathlib import Path

def load_prompt(name: str) -> str:
    prompt_dir = Path("prompts")
    prompt_path = prompt_dir / f"{name}.prompt"
    with open(prompt_path, encoding="utf-8") as f:
        return f.read()