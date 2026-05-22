''' Executing this function initiates the Emotion Detector application
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the emotion_detector function from the package 
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
import json

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emote_detector():
    ''' This code receives the text from the HTML interface and 
        runs detection over it using emotion_detector()
        function. The output returned shows the dominant emotion
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    emotions_dict = json.loads(response)
    print(type(emotions_dict))
    print(emotions_dict)
    anger_score = emotions_dict['anger']
    disgust_score = emotions_dict['disgust']
    fear_score = emotions_dict['fear']
    joy_score = emotions_dict['joy']
    sadness_score = emotions_dict['sadness']
    dominant_emotion = emotions_dict['dominant_emotion']

    if (dominant_emotion == 'None'):
        return "Invalid text! Please try again"
    else:
        return f"""For the given statement, the system
           response is 'anger': {anger_score},
           'disgust': {disgust_score}, 'fear':
           {fear_score}, 'joy': {joy_score} and
           'sadness': {sadness_score}. The dominant
           emotion is {dominant_emotion}. """

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0",port=5000)
