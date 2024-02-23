from flask import render_template
from LyzrControllers import LyzrInitiallizer


data_analysr = LyzrInitiallizer.lyzr_initiallizer()

def insightflow():
    return render_template('insightflow.html')

def datadescription():
    description = data_analysr.dataset_description()
    return render_template('datadescription.html', description=description)


def dataqueries():
    queries = data_analysr.ai_queries_df()
    queries = queries.split('\n')
    return render_template('queries.html', queries=queries)

def analysis_recommendation():
    analysis_recommendation = data_analysr.analysis_recommendation()
    analysis_recommendation = analysis_recommendation.split('\n')
    return render_template('analysis_recommendation.html', analysis_recommendation=analysis_recommendation)