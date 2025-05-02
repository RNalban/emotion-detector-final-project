import requests
import json
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj =  { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url,json=myobj,headers=header)

    if response.status_code ==200:
        formatted_response = json.loads(response.text)
        emotion = formatted_response['emotionPredictions'][0]['emotionMentions'][0]['emotion']
        anger_score=emotion.get('anger')
        joy_score=emotion.get('joy')
        fear_score=emotion.get('fear')
        disgust_score=emotion.get('disgust')
        sadness_score=emotion.get('sadness')
        dominant_emotion= max(emotion,key=emotion.get)
    elif response.status_code ==500:
        anger_score = joy_score = fear_score = disgust_score = sadness_score = dominant_emotion=None
    else:
    # Handle unexpected status codes
        anger_score = joy_score = fear_score = disgust_score = sadness_score = dominant_emotion = None

    return {'anger': anger_score,'disgust': disgust_score,'fear': fear_score,
    'joy': joy_score,'sadness': sadness_score,'dominant_emotion': dominant_emotion}