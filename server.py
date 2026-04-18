from flask import Flask, request, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>Emotion Detector</h2>
    <form method="POST" action="/detect">
        <input type="text" name="text" placeholder="Enter text">
        <input type="submit" value="Analyze">
    </form>
    '''

@app.route('/detect', methods=['POST'])
def detect():
    text = request.form['text']
    result = emotion_detector(text)
    return f"<h3>Result: {result}</h3>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
