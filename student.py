from flask import render_template, request, redirect, session
from flask_login import login_required, current_user
from datetime import datetime

from models import Exam, Question, Result, Answer, db


def init_app(app):

    # student dashboard
    @app.route("/student/dashboard")
    @login_required
    def student_dashboard():
        exams = Exam.query.all()
        return render_template(
            "student_dashboard.html",
            exams=exams
        )

    # start / submit-exam
    @app.route("/student/start-exam/<int:exam_id>", methods=["GET", "POST"])
    @login_required
    def start_exam(exam_id):

        exam = Exam.query.get_or_404(exam_id)
        questions = Question.query.filter_by(exam_id=exam_id).all()

        # exam start 
        if request.method == "GET":
            # Store exam start time in session (ANTI-CHEATING)
            session["exam_start_time"] = datetime.now().timestamp()
            session["exam_id"] = exam_id

            return render_template(
                "start_exam.html",
                exam=exam,
                questions=questions,
                duration=exam.duration
            )

        # exam submit
        if request.method == "POST":

            # server side time validation
            start_time = session.get("exam_start_time")

            if not start_time:
                return "Session expired. Please restart the exam."

            time_taken = datetime.now().timestamp() - start_time

            if time_taken > exam.duration * 60:
                return "Time exceeded. Exam auto-submitted."

            # create result
            score = 0

            result = Result(
                user_id=current_user.id,
                exam_id=exam_id,
                score=0,
                total_questions=len(questions)
            )
            db.session.add(result)
            db.session.commit()

            # evaluate answers
            for q in questions:
                selected = request.form.get(f"question_{q.id}")

                if selected == q.correct_option:
                    score += 1

                answer = Answer(
                    result_id=result.id,
                    question_id=q.id,
                    selected_option=selected
                )
                db.session.add(answer)

            # update score
            result.score = score
            db.session.commit()

            # clean session
            session.pop("exam_start_time", None)
            session.pop("exam_id", None)

            return redirect(f"/student/result/{result.id}")

    # result page
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

        return render_template(
            "result.html",
            exam=exam,
            result=result,
            answers=answers
        )

