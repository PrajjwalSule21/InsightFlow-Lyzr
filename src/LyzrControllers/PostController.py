from flask import render_template, request
from LyzrControllers import LyzrInitiallizer
import ast

data_analysr = LyzrInitiallizer.lyzr_initiallizer()

def analysis():
    if request.method == 'POST':
        query = request.form.get('query')
        analysis = data_analysr.analysis_insights(user_input=query)
        analysis_lst = analysis.split('\n')
        return render_template('analysis.html', analysis_lst=analysis_lst)
    else:
        return render_template('analysis.html')
    


def  recommendation():
    if request.method == 'POST':
        query = request.form.get('query')
        recommendation = data_analysr.recommendations(user_input=query)
        recommendation_dict = ast.literal_eval(recommendation)
        return render_template('recommendation.html', recommendation_dict=recommendation_dict)
    else:
        return render_template('recommendation.html')
    

def tasks():
    if request.method == "POST":
        query = request.form.get('query')
        tasks = data_analysr.tasks(user_input=query)
        tasks_lst = tasks.split('\n')
        return render_template('tasks.html', tasks_lst =  tasks_lst)
    else:
        return render_template('tasks.html')

