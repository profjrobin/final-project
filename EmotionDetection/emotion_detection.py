"""Function to run emotion detection"""
import json
import requests

def emotion_detector(text_to_analyze):
    """Run emotion detection from Watson embedded APIs"""
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input_json, headers = headers)

    if (response.status_code == 200):
        # Convert response to a dictionary
        data_dict = json.loads(response.text)

        #emotionPredictions is a list of iems
        emotions = data_dict['emotionPredictions'][0]['emotion']

        dominant_emotion = max(emotions, key=emotions.get)
    elif (response.status_code == 400):
        emotions = {'anger': 'None', 'disgust': 'None', 'fear': 'None',
        'joy': 'None', 'sadness': 'None'}
        dominant_emotion = None

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    return f"""
    {{
        "anger": "{anger_score}",
        "disgust": "{disgust_score}",
        "fear": "{fear_score}",
        "joy": "{joy_score}",
        "sadness": "{sadness_score}",
        "dominant_emotion": "{dominant_emotion}"
     }}
     """
     