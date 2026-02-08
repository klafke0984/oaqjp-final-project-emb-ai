import requests

def emotion_detector(text_to_analyse):

    url = (
    "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1"
    "/NlpService/EmotionPredict"
)            
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = input_json, headers = header)

    if response.status_code == 200:
        return response.text
    else:
        return {"error": response.status_code, "message": response.text}

#if __name__ == '__main __':
#    emotion_detector()