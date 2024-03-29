# One-to-many relationships

from main import db

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.Text)
    description = db.Column(db.Text)
    due_date = db.Column(db.DateTime)
    completed_at = db.Column(db.DateTime, nullable=True)

    # user_id
