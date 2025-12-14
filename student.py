from flask import render_template, request, redirect
from flask_login import login_required, current_user
from models import Exam, Question, Result, Answer, db

def init_app(app):

    @app.route("/student/dashboard")
    @login_required
    def student_dashboard():
        exams = Exam.query.all()
        return render_template("student_dashboard.html", exams=exams)

    @app.route("/student/start-exam/<int:exam_id>", methods=["GET", "POST"])
    @login_required
    def start_exam(exam_id):
        exam = Exam.query.get_or_404(exam_id)
        questions = Question.query.filter_by(exam_id=exam_id).all()

        if request.method == "POST":
            score = 0
            result = Result(
                user_id=current_user.id,
                exam_id=exam_id,
                score=0,
                total_questions=len(questions)
            )
            db.session.add(result)
            db.session.commit()

            for q in questions:
                selected = request.form.get(f"question_{q.id}")
                if selected == q.correct_option:
                    score += 1

                db.session.add(Answer(
                    result_id=result.id,
                    question_id=q.id,
                    selected_option=selected
                ))

            result.score = score
            db.session.commit()

            return redirect(f"/student/result/{result.id}")

        return render_template(
            "start_exam.html",
            exam=exam,
            questions=questions,
            duration=exam.duration
        )

    @app.route("/student/result/<int:result_id>")
    @login_required
    def result(result_id):
        result = Result.query.get_or_404(result_id)
        exam = Exam.query.get(result.exam_id)

        answers = (
            db.session.query(Answer, Question)
            .join(Question, Answer.question_id == Question.id)
            .filter(Answer.result_id == result.id)
            .all()
        )

        return render_template("result.html", exam=exam, result=result, answers=answers)
