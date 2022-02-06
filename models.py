from sqlalchemy import Column, Integer, String
from database import Base

class Record(Base):
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    azet = Column(String(200), unique=True)

    def __init__(self, name=None, email=None, azet=None):
        self.name = name
        self.email = email
        self.azet = azet

    def __repr__(self):
        return f'<User {self.name!r}>'