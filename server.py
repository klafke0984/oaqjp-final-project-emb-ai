'''
    This module creates a server using Flask to connect 
    NLP Emotion Detection application to IBM's Watson NLP.
'''
# Import necessary packages
from flask import Flask, render_template, request
from EmotionDetection import emotion_detection

app = Flask('__name__')

@app.route('/')
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector():
    ''' This function gets the user entered phrase to analyze and uses Watson NLP
        to provide feedback to the user
    '''
    # Gets the text from the user input on the index.html page
    text_to_analyze = request.args.get('textToAnalyze')

    # Dictionary with emotions and respective scores from Watson NLP
    emotion = emotion_detection.emotion_detector(text_to_analyze)

    # If dominant emotion is None return invalid input message to user
    if emotion['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    # Return emotion statement based on user input.
    return(
        f"For the given statement, the system response is 'anger': {emotion['anger']}, "
        f"'disgust': {emotion['disgust']}, 'fear': {emotion['fear']}, "
        f"'joy': {emotion['joy']} and 'sadness': {emotion['sadness']}. "
        f"The dominant emotion is {emotion['dominant_emotion']}."
    )

if __name__ == "__main__":
    # Calls Flask run function to deploy app on localhost
    app.run(host="0.0.0.0", port=5000)
