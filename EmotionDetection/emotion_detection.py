import requests
import json

emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']

def emotion_detector(text_to_analyze):
    """
    Function for analyzing sentiments with Watson.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {'raw_document': {'text': text_to_analyze} }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)
    result = {}
    try:
        result = formatted_response["emotionPredictions"][0]["emotion"]
        result['dominant_emotion'] = ''
    except KeyError:
        pass
    
    max_value = 0

    if response.status_code == 400:
        for i in range(len(emotions)):
            result[emotions[i]] = None
    else:
        for key, value in result.items():
            if isinstance(value, float) and value > max_value:
                result['dominant_emotion'] = key
                max_value = value

    return result

emotion_detector('I love learning!')