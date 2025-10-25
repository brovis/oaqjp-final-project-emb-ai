'''
This is the file responsible to calculate Emotion.
Author: Rohit Bohra
'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

my_app=Flask('Emotion detection')

@my_app.route('/emotionDetector', methods=['GET'])
def emotiondetector():
    '''
    This is the method to calculate the Emotion 
    when route /emotionDetector is being used
    '''
    text_to_analyze=request.args.get('textToAnalyze')
    response=emotion_detector(text_to_analyze)
    dominant_emotion=response["dominant_emotion"]
    if dominant_emotion is None:
        return {'message': 'Invalid Text! Please try again'}
    emotion_str = ", ".join([f"'{k}': '{v}'" for k, v in response.items() if k!="dominant_emotion"])
    final_response = (
    f"For the given statement, the system response is {emotion_str}. "
    f"The dominant emotion is {dominant_emotion}."
    )
    return final_response


@my_app.route("/")
def render_index_page():
    '''
    this is the index method to load the main page.
    '''
    return render_template('index.html')

if __name__ == "__main__":
    my_app.run(host="0.0.0.0", port=5000)
