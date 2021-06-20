from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from views import Assessment, Document

app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(Assessment, '/')
api.add_resource(Document, '/document')

if __name__ == "__main__":
    app.run()
