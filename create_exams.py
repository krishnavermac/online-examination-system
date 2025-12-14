from app import app
from models import db, Exam

with app.app_context():
    if Exam.query.count() == 0:
        exams = [
            Exam(title="Python Basics", description="Fundamentals of Python"),
            Exam(title="Flask Fundamentals", description="Flask framework basics"),
            Exam(title="Database Systems", description="SQL and ORM concepts"),
        ]

        db.session.add_all(exams)
        db.session.commit()
        print("Exams added")
    else:
        print("Exams already exist")
