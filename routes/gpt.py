from flask import Blueprint, request, jsonify
from services.gpt_service import summarize_text, chat_with_context

gpt_bp = Blueprint('gpt', __name__)

@gpt_bp.route('/gpt/summarize', methods=['POST'])
def summarize_route():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "텍스트 없음."}), 400

    try:
        summary = summarize_text(text)
        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@gpt_bp.route('/gpt/chat', methods=['POST'])
def chat_route():
    data = request.get_json()
    question = data.get("question", "")

    if not question:
        return jsonify({"error": "텍스트 없음."}), 400

    try:
        answer = chat_with_context(question)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
