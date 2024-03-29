from main import db

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.Text)
    description = db.Column(db.Text)
    due_date = db.Column(db.DateTime)
    completed_at = db.Column(db.DateTime, nullable=True, default=None)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship(
        "User",
        back_populates="tasks"
    )


# I am teacher - Akash
# Job vacancy in Zendesk (1 vacancy)
# Task (apply for job) -> 
# user_id = 4
