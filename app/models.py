from app.database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True)
    password = Column(String)

class Avto(Base):
    __tablename__ = "avto"
    id = Column(Integer, primary_key=True)
    brand = Column(String)
    model = Column(String)
    year = Column(Integer)
