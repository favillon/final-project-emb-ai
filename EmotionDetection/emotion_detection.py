import requests 
import json

def emotion_detector(text_to_analyse):
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    
    print(response)
    print(formatted_response)
    
    if response.status_code == 200:
        anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        object_emotion = {
            'anger': anger, 
            'disgust': disgust,
            'fear': fear, 
            'joy': joy,
            'sadness': sadness
        }
        object_emotion['dominant_emotion'] =  find_predominant_emotion(object_emotion)
    
    elif response.status_code == 400:
        object_emotion = {
            'anger': None, 
            'disgust': None,
            'fear': None, 
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    return object_emotion

def find_predominant_emotion(emotions):
  return max(emotions, key=emotions.get)