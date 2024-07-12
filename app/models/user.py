from flask_login import UserMixin

from .. import login_manager 
from ..db_manager import DBManager
from .base import BaseModel

db_manager = DBManager()
db = db_manager.get_db()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(BaseModel,UserMixin):
    __tablename__ = 'user'
    username = db.Column(db.String(25),unique=True, nullable=False)
    password = db.Column(db.String(125),nullable=False)
    email = db.Column(db.String(256))

    def __repr__(self):
        return f"User('{self.username}')"
