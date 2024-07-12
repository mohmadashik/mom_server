from ..db_manager import DBManager
db_manager =DBManager()
db = db_manager.get_db()


class BaseModel(db.Model):
    """abstract base class method"""
    __abstract__ = True
    id = db.Column(db.Integer,primary_key=True)
    created_at = db.Column(db.String(30),index=False,nullable=False)
    modified_at= db.Column(db.String(30),index=False,nullable=True)
    created_by = db.Column(db.Integer)
    modified_by = db.Column(db.Integer)