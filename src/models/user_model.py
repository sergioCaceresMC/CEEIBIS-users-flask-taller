import uuid
from utils.db import db
from datetime import datetime
from sqlalchemy import Column, String, DateTime 

class User(db.Model):
    __tablename__ = "user"
    
    id = Column(String(36), primary_key = True, default = lambda: str(uuid.uuid4()))
    username = Column(String(20), nullable=False, unique=True)
    name = Column(String(40), nullable=False, unique=False)
    lastname = Column(String(40), nullable=False, unique=False)
    email = Column(String(400), nullable=False, unique=False)
    created_at = Column(DateTime, default=datetime.now())

    def __init__(self, name, lastname, username, email):
        self.username = username
        self.name = name
        self.lastname = lastname
        self.email = email
    
    def __str__(self):
        return {
            'username': self.username, 
        }
    