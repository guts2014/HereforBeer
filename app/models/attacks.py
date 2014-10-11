from app import db
from sqlalchemy import Column, Integer, Text, Datetime

class Attack(db.Model):

    __tablename__ = 'attacks'

    event_id = Column(db.Integer, primary_key=True)

