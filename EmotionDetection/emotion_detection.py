import requests
import json

def emotion_detector(text_to_analyse):
    URL ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_obj= {"raw_document": {"text": text_to_analyse}}
    response= requests.post(url=URL, headers=Headers, json=input_obj)
    if response.status_code==200:
        formated_response= json.loads(response.text)
        emotions= formated_response["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotions, key=emotions.get)
        emotions['dominant_emotion']= dominant_emotion
        return emotions
    elif response.status_code==400 or response.status_code==500:
        return ({
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
      })
    