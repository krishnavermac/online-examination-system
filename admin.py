from flask import render_template, request, redirect
from flask_login import login_required, current_user
from sqlalchemy import func

from models import Exam, Question, Result, Answer, db


def init_app(app):

    # ================= ADMIN DASHBOARD =================
    @app.route("/admin/dashboard")
    @login_required
    def admin_dashboard():
        if current_user.role != "admin":
            return "Unauthorized access"

        exams = Exam.query.all()
        return render_template(
            "admin_dashboard.html",
            exams=exams
        )

    # ================= CREATE EXAM =================
    @app.route("/admin/create-exam", methods=["GET", "POST"])
    @login_required
    def create_exam():
        if current_user.role != "admin":
            return "Unauthorized access"

        if request.method == "POST":
            exam = Exam(
                title=request.form["title"],
                duration=int(request.form["duration"]),
                description=request.form.get("description", "")
            )
            db.session.add(exam)
            db.session.commit()
            return redirect("/admin/dashboard")

        return render_template("create_exam.html")

    # ================= ADD QUESTION =================
    @app.route("/admin/add-question/<int:exam_id>", methods=["GET", "POST"])
    @login_required
    def add_question(exam_id):
        if current_user.role != "admin":
            return "Unauthorized access"

        exam = Exam.query.get_or_404(exam_id)

        if request.method == "POST":
            question = Question(
                exam_id=exam_id,
                question_text=request.form["question"],
                option_a=request.form["option_a"],
                option_b=request.form["option_b"],
                option_c=request.form["option_c"],
                option_d=request.form["option_d"],
                correct_option=request.form["correct_option"]
            )
            db.session.add(question)
            db.session.commit()
            return redirect("/admin/dashboard")

        return render_template("add_question.html", exam=exam)

    # ================= ANALYTICS DASHBOARD =================
    @app.route("/admin/analytics")
    @login_required
    def analytics():
        if current_user.role != "admin":
            return "Unauthorized access"

        analytics_data = (
            db.session.query(
                Exam.id,
                Exam.title,
                func.count(Result.id).label("attempts"),
                func.avg(Result.score).label("avg_score"),
                func.max(Result.score).label("max_score"),
                func.min(Result.score).label("min_score")
            )
            .outerjoin(Result, Exam.id == Result.exam_id)
            .group_by(Exam.id)
            .all()
        )

        return render_template(
            "analytics.html",
            analytics_data=analytics_data
        )
