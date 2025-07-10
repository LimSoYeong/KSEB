from flask import Blueprint, request, jsonify
from services.ocr_engine import extract_text_from_image

ocr_bp = Blueprint('ocr', __name__)

@ocr_bp.route("/ocr", methods=["POST"])
def ocr_route():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "이미지 없음."}), 400

        image = request.files['image']
        extracted_text = extract_text_from_image(image)

        return jsonify({"text": extracted_text})

    except Exception as e:
        #디버깅
        print(f"예외: {e}")
        return jsonify({"error": str(e)}), 500
