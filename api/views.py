from db import Db
from flask import request
from flask_restful import Resource
from sqlalchemy import text as sql_text


class Assessment(Resource):
    """ The Assessments View """

    def __init__(self):
        self.db = Db()

    def get(self):
        """ Returns a list of assessments """
        query = "SELECT * FROM assessment"
        res = self.db.connection.execute(query)
        rows = res.fetchall()
        keys = res.keys()
        assessments = self.db.clean_select_results(rows, keys)

        return {
            'assessments': assessments
        }

    def post(self):
        """
        Add a assessment to the db 
        Expect a JSON payload with the following format
        {
            "course_course_id": <INT>,
            "topic": "The topic of the assessment",
            "state": "The current state of the assessment"
            "is_rated": <BOOLEAN>
            "max_rating": <INT>
            "rating": <INT>
        }
        """
        data = request.get_json()
        query = "INSERT INTO `assessment` (`course_course_id`, `topic`, `state`, `is_rated`, `max_rating`, `rating`) VALUES (:course_course_id, :topic, :state, :is_rated, :max_rating, :rating)"
        try:
            self.db.connection.execute(sql_text(query), data)
            return True
        except:
            return False


class Document(Resource):
    """ The Documents View """

    def __init__(self):
        self.db = Db()

    def get(self):
        """ Returns a list of documents regarding the given assessment id """
        query = "SELECT * FROM document"
        res = self.db.connection.execute(query)
        rows = res.fetchall()
        keys = res.keys()
        documents = self.db.clean_select_results(rows, keys)

        return {
            'documents': documents
        }

    def post(self):
        """
        Add a document to the db 
        Expect a JSON payload with the following format
        {
            "name": "Name of the document",
            "data": "Blob data",
        }
        """
        data = request.get_json()
        query = "INSERT INTO `assessment` (`name`, `data`) VALUES (:name, :data)"
        try:
            self.db.connection.execute(sql_text(query), data)
            return True
        except:
            return False
