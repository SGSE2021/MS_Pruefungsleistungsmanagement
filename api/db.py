from datetime import date, datetime
from decimal import Decimal
import os

from sqlalchemy import create_engine


class Db():
    def __init__(self):
        # Dev: mysql+pymysql://dbuser:dbpassword@db/assessment_db
        # Prod: mysql+pymysql://examsdb-user:h5qbbl8CEb@exams-mysql.support.svc.cluster.local:3306/examdb
        db_url = os.getenv('DATABASE_URL')

        engine = create_engine(db_url)
        self.connection = engine.connect()

    def __del__(self):
        self.connection.close()

    def clean_select_row(self, row, keys):
        try:
            clean_row = [str(field) if isinstance(field, datetime) or isinstance(
                field, Decimal) or isinstance(field, date) else field for field in list(row)]
            current_row = {}
            for i in range(len(keys)):
                current_row[keys[i]] = clean_row[i]
            return current_row
        except:
            return None

    def clean_select_results(self, data, keys):
        if len(data) == 0:
            return {}
        result_data = []
        for row in data:
            result_data.append(self.clean_select_row(row, keys))
        return result_data
