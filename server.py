from flask import Flask, render_template, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    text_to_analyze = request.form.get("text", "")

    if not text_to_analyze.strip():
        return jsonify({"error": "Input text cannot be blank"}), 400

    result = emotion_detector(text_to_analyze)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
