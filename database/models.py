from sqlalchemy import Column,  ForeignKey, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Widget(db.Model):
    __tablename__ = 'widgets'

    widget_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Thing(db.Model):
    __tablename__ = 'things'

    thing_id = Column(Integer, primary_key=True)
    widget_id = Column(Integer, ForeignKey('widgets.widget_id'), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
