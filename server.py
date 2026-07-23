from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route("/emotionDetector")
def check_analysis():
    text_to_analyze = request.args['analyze']
    response = emotion_detector(text_to_analyze)
    return jsonify(response), 200

@app.route("/")
def render_template():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

