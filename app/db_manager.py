from flask_sqlalchemy import SQLAlchemy

class DBManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DBManager,cls).__new__(cls)
            cls._instance.db = SQLAlchemy()
        return cls._instance
    

    @classmethod
    def get_db(cls):
        return cls._instance.db 