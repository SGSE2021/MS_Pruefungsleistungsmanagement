from db import Db
from flask import request
from flask_restful import Resource
from sqlalchemy import text as sql_text


class Assessment(Resource):
    """ The Assessment View """

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
            "course_course_id": int,
            "start_date": str,
            "end_date": str,
            "topic": str,
            "state": str,
            "is_rated": bool,
            "max_rating": int
        }
        """
        data = request.get_json()
        query = "INSERT INTO `assessment` (`course_course_id`, `topic`, `start_date`, `end_date`, `state`, `is_rated`, `max_rating`) VALUES (:course_course_id, :topic, :start_date, :end_date, :state, :is_rated, :max_rating)"
        last_row_id = "SELECT assessment_id FROM `assessment` ORDER BY `assessment_id` DESC LIMIT 1;"
        try:

            self.db.connection.execute(sql_text(query), data)
            res = self.db.connection.execute(sql_text(last_row_id))
            rows = res.fetchall()
            keys = res.keys()
            assessment_id = self.db.clean_select_results(rows, keys)
            return {
                'assessment_id': assessment_id
            }
        except:
            return False


class SingleAssessment(Resource):
    """ The Single Assessment View """

    def __init__(self):
        self.db = Db()

    def get(self, assessment_id):
        """ Returns specific assessment by ID"""
        query = "SELECT * FROM assessment WHERE assessment_id=%s"
        data_tuple = (assessment_id)
        request.args.get("")
        res = self.db.connection.execute(query, data_tuple)
        rows = res.fetchall()
        keys = res.keys()
        assessment = self.db.clean_select_results(rows, keys)

        return {
            'assessment': assessment
        }

    def put(self, assessment_id):
        data = request.get_json()
        query = """UPDATE assessment SET topic=%s, state=%s, is_rated=%s, max_rating=%s, rating=%s WHERE assessment_id=%s"""
        data_tuple = (data["topic"], data["state"], data["is_rated"],
                      data["max_rating"], data["rating"], assessment_id)
        try:
            self.db.connection.execute(query, data_tuple)
            return True
        except:
            return False

    def delete(self, assessment_id):
        query = """DELETE FROM assessment WHERE assessment_id=%s"""
        data_tuple = (assessment_id)
        try:
            self.db.connection.execute(query, data_tuple)
            return True
        except:
            return False


class Question(Resource):
    """ The Question View """

    def __init__(self):
        self.db = Db()

    def get(self):
        query = "SELECT * FROM question"
        res = self.db.connection.execute(query)
        rows = res.fetchall()
        keys = res.keys()
        questions = self.db.clean_select_results(rows, keys)

        return {
            'questions': questions
        }

    def post(self):
        """
        Add a question to the db 
        Expect a JSON payload with the following format
        {
            "assessment_assessment_id": int,
            "is_multiple_choice": bool,
            "question": str,
            "points": int
        }
        """
        data = request.get_json()
        query = "INSERT INTO `question` (`assessment_assessment_id`, `is_multiple_choice`, `question`, `points`) VALUES (:assessment_assessment_id, :is_multiple_choice, :question, :points)"
        last_row_id = "SELECT question_id FROM `question` ORDER BY `question_id` DESC LIMIT 1;"
        try:
            self.db.connection.execute(sql_text(query), data)
            res = self.db.connection.execute(sql_text(last_row_id))
            rows = res.fetchall()
            keys = res.keys()
            question_id = self.db.clean_select_results(rows, keys)
            return {
                'question_id': question_id
            }
        except:
            return False


class AssessmentQuestion(Resource):

    def __init__(self):
        self.db = Db()

    def get(self, assessment_id):
        """ Returns questions by assessment ID"""
        query = "SELECT * FROM question WHERE assessment_assessment_id=%s"
        data_tuple = (assessment_id)
        request.args.get("")
        res = self.db.connection.execute(query, data_tuple)
        rows = res.fetchall()
        keys = res.keys()
        questions = self.db.clean_select_results(rows, keys)

        return {
            'questions': questions
        }


class SingleQuestion(Resource):
    """ The Single Question View """

    def __init__(self):
        self.db = Db()

    def get(self, question_id):
        """ Returns specific question by ID"""
        query = "SELECT * FROM question WHERE question_id=%s"
        data_tuple = (question_id)
        request.args.get("")
        res = self.db.connection.execute(query, data_tuple)
        rows = res.fetchall()
        keys = res.keys()
        question = self.db.clean_select_results(rows, keys)

        return {
            'question': question
        }

    def put(self, question_id):
        data = request.get_json()
        query = """UPDATE question SET points=%s, answer=%s, reached_score=%s WHERE question_id=%s"""
        data_tuple = (data["points"], data["answer"],
                      data["reached_score"], question_id)
        try:
            self.db.connection.execute(query, data_tuple)
            return True
        except:
            return False

    def delete(self, question_id):
        query = """DELETE FROM question WHERE question_id=%s"""
        data_tuple = (question_id)
        try:
            self.db.connection.execute(query, data_tuple)
            return True
        except:
            return False


class Answer(Resource):
    """ The Answers View """

    def __init__(self):
        self.db = Db()

    def get(self):
        query = "SELECT * FROM answer"
        res = self.db.connection.execute(query)
        rows = res.fetchall()
        keys = res.keys()
        answers = self.db.clean_select_results(rows, keys)

        return {
            'answers': answers
        }

    def post(self):
        """
        Add an answer to the db 
        Expect a JSON payload with the following format
        {
            "question_question_id": int,
            "answer_text": str,
            "is_correct": bool,
            "is_checked": bool
        }
        """
        data = request.get_json()
        query = "INSERT INTO `answer` (`question_question_id`, `answer_text`, `is_correct`, `is_checked`) VALUES (:question_question_id, :answer_text, :is_correct, :is_checked)"
        try:
            self.db.connection.execute(sql_text(query), data)
            return True
        except:
            return False


class QuestionAnswer(Resource):

    def __init__(self):
        self.db = Db()

    def get(self, question_id):
        """ Returns answers by question ID"""
        query = "SELECT * FROM answer WHERE question_question_id=%s"
        data_tuple = (question_id)
        request.args.get("")
        res = self.db.connection.execute(query, data_tuple)
        rows = res.fetchall()
        keys = res.keys()
        answers = self.db.clean_select_results(rows, keys)

        return {
            'answers': answers
        }


class SingleAnswer(Resource):
    """ The Answer View """

    def __init__(self):
        self.db = Db()

    def get(self, answer_id):
        """ Returns specific answer by ID"""
        query = "SELECT * FROM answer WHERE answer_id=%s"
        data_tuple = (answer_id)
        request.args.get("")
        res = self.db.connection.execute(query, data_tuple)
        rows = res.fetchall()
        keys = res.keys()
        answer = self.db.clean_select_results(rows, keys)

        return {
            'answer': answer
        }

    def put(self, answer_id):
        data = request.get_json()
        query = """UPDATE answer SET is_checked=%s WHERE answer_id=%s"""
        data_tuple = (data["is_checked"], answer_id)
        try:
            self.db.connection.execute(query, data_tuple)
            return True
        except:
            return False

    def delete(self, answer_id):
        query = """DELETE FROM answer WHERE answer_id=%s"""
        data_tuple = (answer_id)
        try:
            self.db.connection.execute(query, data_tuple)
            return True
        except:
            return False


class Document(Resource):
    """ The Documents View """

    def __init__(self):
        self.db = Db()

    def get(self):
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
            "assessment_assessment_id": int,
            "doc_name": str,
            "doc_data": blob
        }
        """
        data = request.get_json()
        query = "INSERT INTO `document` (`assessment_assessment_id`, `doc_name`, `doc_data`) VALUES (:assessment_assessment_id, :doc_name, :doc_data)"
        try:
            self.db.connection.execute(sql_text(query), data)
            return True
        except:
            return False


class AssessmentDocument(Resource):

    def __init__(self):
        self.db = Db()

    def get(self, assessment_id):
        """ Returns documents by assessment ID"""
        query = "SELECT * FROM document WHERE assessment_assessment_id=%s"
        data_tuple = (assessment_id)
        request.args.get("")
        res = self.db.connection.execute(query, data_tuple)
        rows = res.fetchall()
        keys = res.keys()
        documents = self.db.clean_select_results(rows, keys)

        return {
            'documents': documents
        }


class SingleDocument(Resource):
    """ The Single Documents View """

    def __init__(self):
        self.db = Db()

    def get(self, document_id):
        """ Returns specific document by ID"""
        query = "SELECT * FROM document WHERE document_id=%s"
        data_tuple = (document_id)
        request.args.get("")
        res = self.db.connection.execute(query, data_tuple)
        rows = res.fetchall()
        keys = res.keys()
        document = self.db.clean_select_results(rows, keys)

        return {
            'document': document
        }

    def put(self, document_id):
        data = request.get_json()
        query = """UPDATE document SET assessment_assessment_id=%s, doc_name=%s, doc_data=%s WHERE document_id=%s"""
        data_tuple = (data["assessment_assessment_id"],
                      data["doc_name"], data["doc_data"], document_id)
        try:
            self.db.connection.execute(query, data_tuple)
            return True
        except:
            return False

    def delete(self, document_id):
        query = """DELETE FROM document WHERE document_id=%s"""
        data_tuple = (document_id)
        try:
            self.db.connection.execute(query, data_tuple)
            return True
        except:
            return False
