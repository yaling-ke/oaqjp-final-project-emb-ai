from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_emotion():
    # Retrive the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")
    # Pass the text to the emotion analyzer
    response = emotion_detector(text_to_analyze)

    
    text = ["'"+k+"': "+str(v) for k, v in response.items()]
    text = ", ".join(text[:-1])
    text += ". The dominant emotion is " + response["dominant_emotion"]

    return "For the given statement, the system response is " + text

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)