from app import db
from sqlalchemy import Column, Integer, Text, DateTime

class Event(db.Model):

    __tablename__ = 'events'

    eventid = Column(db.Integer, primary_key=True)
    iyear = Column(db.Integer)
    imonth = Column(db.Integer)
    iday = Column(db.Integer)
