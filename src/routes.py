from flask import Blueprint
from LyzrControllers import GetController, PostController


InsightFlow = Blueprint('InsightFlow', __name__)

InsightFlow.route('/insightflow', methods=['GET'])(GetController.insightflow)
InsightFlow.route('/description', methods=['GET'])(GetController.datadescription)
InsightFlow.route('/queries', methods=['GET'])(GetController.dataqueries)
InsightFlow.route('/analysis-recommendation', methods=['GET'])(GetController.analysis_recommendation)
InsightFlow.route('/analysis', methods=['GET', 'POST'])(PostController.analysis)
InsightFlow.route('/recommendation', methods=['GET', 'POST'])(PostController.recommendation)
InsightFlow.route('/task', methods=['GET', 'POST'])(PostController.tasks)

