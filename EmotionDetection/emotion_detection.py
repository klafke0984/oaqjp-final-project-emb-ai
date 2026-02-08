'''
    This module uses IBM's Watson NLP model to detect emotions based on
    sentences provided by the user.
'''

# Import the necessary modules
import requests

def emotion_detector(text_to_analyse):

    '''
    Sends a post request to IBM's Watson NLP module with the text to analyze

    Args: 
        text_to_analyse (str): The text to be analyzed

    Returns:
        dict: A formatted dictionary with possible emotions and the score.

    Raises:
        Response.status_code: If error in the post request.
    '''

    url = (
    "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1"
    "/NlpService/EmotionPredict"
)            
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = input_json, headers = header)

    if response.status_code == 200:
        # Formats the response to JSON
        emotions = response.json()

        # Creates a dictionary with the emotions
        emotions_dict = emotions['emotionPredictions'][0]['emotion']

        # Selects the top emotion based on the highest score
        top_emotion = max(emotions_dict, key = emotions_dict.get)

        # Generate dictionary with all emotions and respective scores
        emotion = {
            'anger' : emotions_dict['anger'],
            'disgust' : emotions_dict['disgust'],
            'fear' : emotions_dict['fear'],
            'joy' : emotions_dict['joy'],
            'sadness' : emotions_dict['sadness'],
            'dominant_emotion' : top_emotion
        }

        return emotion
    
    else:
        # Return error message to user in case of error
        return {"error": response.status_code, "message": response.text}
