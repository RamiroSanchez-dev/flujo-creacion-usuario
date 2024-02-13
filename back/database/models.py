from sqlalchemy import Column, Integer, String, Text,ForeignKey,Boolean, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    email = Column(String(255),primary_key=True, index=True)
    contry = Column(String(10), index=True)
    fullName = Column(String(200))
    userName = Column(String(200))
    age = Column(Integer)


