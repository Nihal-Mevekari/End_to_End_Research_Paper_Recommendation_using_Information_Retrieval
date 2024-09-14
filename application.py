import os
import pandas as pd
from flask import Flask, request, render_template

from src.pipeline.predict_pipeline import PredictPipeline
from src.utils import load_object

application=Flask(__name__)

app=application

##Route for a home page
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():

    if request.method=='GET':
        return render_template('home.html')
    else:
        query = request.form.get('query_paper')
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(query)

        if results == "Invalid search..Try again":
            return render_template('error_page.html', message="Invalid search..Try again")
        else:
            similar_papers = []
            for paper in results['papers']['titles']:
                similar_papers.append(paper)
            return render_template('home.html', paper=similar_papers)
    

if __name__ == "__main__":
    app.run()