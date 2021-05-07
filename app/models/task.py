from flask import current_app
from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime(), nullable=True)
    is_complete = False

    def as_dict(self):
        task = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "is_complete": True if self.completed_at else False
        }