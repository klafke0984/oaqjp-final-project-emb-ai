import requests
from flask import Flask

app = Flask('__name__')

@app.route('/')
def index():

@app.route('/emotionDetector')
    def emotion_detector():

        print(f"For the given statement, the system response is 'anger': 0.006274985, 'disgust': 0.0025598293, 'fear': 0.009251528, 'joy': 0.9680386 and 'sadness': 0.049744144. The dominant emotion is {dominant_emotion}.")