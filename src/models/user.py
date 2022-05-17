from common.db import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class User(db.Model):
    __tablename__ = "user"

    username = db.Column(db.String(32), primary_key=True)
    password_hash = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
