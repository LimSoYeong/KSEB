from flask import Flask
from routes.ocr import ocr_bp
from routes.tts import tts_bp
from routes.gpt import gpt_bp
from routes.stt import stt_bp

app = Flask(__name__)

app.register_blueprint(ocr_bp)
app.register_blueprint(tts_bp)
app.register_blueprint(gpt_bp)
app.register_blueprint(stt_bp)

if __name__ == "__main__":
    app.run(debug=True)
