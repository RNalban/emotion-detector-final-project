"""Flask app for detecting emotion from user input text."""

from flask import Flask, render_template, request
from main.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("Emotion Detector")


@app.route("/")
def render_text_page():
    """Render the index HTML page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detect():
    """Process the text input and return the detected emotion and its score."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid Text! Please Try again!"

    score = response[dominant_emotion]
    return (
    f"The given statement emotion has been identified as "
    f"{dominant_emotion} with score {score}"
)

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
