from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from views import Assessment, SingleAssessment, Question, SingleQuestion, Answer, SingleAnswer, Document, SingleDocument

app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(Assessment, '/assessments')
api.add_resource(SingleAssessment, '/assessments/<assessment_id>')

api.add_resource(Question, '/assessments/questions')
api.add_resource(SingleQuestion, '/assessments/questions/<question_id>')

api.add_resource(Answer, '/assessments/questions/answers')
api.add_resource(SingleAnswer, '/assessments/questions/answers/<answer_id>')

api.add_resource(Document, '/assessments/documents')
api.add_resource(SingleDocument, '/assessments/documents/<document_id>')


if __name__ == "__main__":
    app.run()
