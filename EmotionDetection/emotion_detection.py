import requests
import json

def emotion_detector(text_to_analyze):
    """
    Function for analyzing sentiments with Watson.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {'raw_document': {'text': text_to_analyze} }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)
    result = formatted_response["emotionPredictions"][0]["emotion"]
    result['dominant_emotion'] = ''
    max_value = 0
    for key, value in result.items():
        try:
            if value > max_value:
                result['dominant_emotion'] = key
                max_value = value
        except TypeError:
            pass

    return result

emotion_detector('I love learning!')