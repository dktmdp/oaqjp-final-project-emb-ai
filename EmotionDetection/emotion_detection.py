import requests
import json

url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

def emotion_detector(text_to_analyze):
    response = requests.post(
        url,
        json={ "raw_document": { "text": text_to_analyze } },
        headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    )
    formatted_response =  json.loads(response.text)
    emotion =  formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion, key=emotion.get)
    return {
        **emotion,
        "dominant_emotion": dominant_emotion
    }