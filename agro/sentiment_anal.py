import os
from flask import Flask, render_template, request, current_app, jsonify,  url_for, redirect
import io
import base64
import logging
import json
from werkzeug import secure_filename
import nltk
import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

app = Flask(__name__)
#ALLOWED_EXTENSIONS = set(list(['png', 'jpg', 'jpeg']))
#UPLOAD_FOLDER = os.path.basename('/static')
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#print('Sfter app config')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/level1')
def level1():
    return render_template('level1.html')

@app.route('/level2')
def level2():
    return render_template('level2.html')

@app.route('/level3')
def level3():
    return render_template('level3.html')

@app.route('/next')
def next():
    return render_template('next.html')

@app.route('/level4')
def level4():
    return render_template('level4.html')
@app.route('/level5')
def level5():
    return render_template('level5.html')
@app.route('/level6')
def level6():
    return render_template('level6.html')





@app.route('/getResults',  methods=['GET', 'POST'])

def getResults():
    if request.method == 'POST':
	input_Txt = request.form.get('sText')
        
	json_prediction = predict(input_Txt)
	if (json_prediction):
	   return render_template("next.html", result = json_prediction)
	else:
	    return render_template("level6.html")

    else:
        return render_template("level3.html")

def sentiment_result(fb_post):	
	sia = SentimentIntensityAnalyzer()
	ss = sia.polarity_scores(fb_post)
	s_result = ss['compound']
	if (s_result < 0.5):
	   mood = True	
    	else:
	   mood = False
	
	return mood

def predict(input_Txt):
    predictions = sentiment_result(input_Txt)
    return predictions

@app.route('/result_page/<json_prediction>')
def result_page(json_prediction):
    return  'Here are the results %s ' % json_prediction

if __name__ == '__main__':
	app.run(host='localhost', port=8080, debug=True)
