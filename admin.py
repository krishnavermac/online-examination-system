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
            title = request.form.get("title")
            duration = request.form.get("duration")
            description = request.form.get("description", "")

            if not title or not duration:
                return "Invalid exam data", 400

            exam = Exam(
                title=title,
                duration=int(duration),
                description=description
            )
            db.session.add(exam)
            db.session.commit()

            return redirect("/admin/dashboard")

        return render_template("create_exam.html")

    # ================= ADD QUESTION (FIXED) =================
    @app.route("/admin/add-question/<int:exam_id>", methods=["GET", "POST"])
    @login_required
    def add_question(exam_id):
        if current_user.role != "admin":
            return "Unauthorized access"

        exam = Exam.query.get_or_404(exam_id)

        if request.method == "POST":
            question_text = request.form.get("question_text")
            option_a = request.form.get("option_a")
            option_b = request.form.get("option_b")
            option_c = request.form.get("option_c")
            option_d = request.form.get("option_d")
            correct_option = request.form.get("correct_option")

            # Validation (prevents BadRequestKeyError)
            if not all([question_text, option_a, option_b, option_c, option_d]):
                return "All fields are required", 400

            if correct_option not in ["A", "B", "C", "D"]:
                return "Invalid correct option", 400

            question = Question(
                exam_id=exam_id,
                question_text=question_text,   # ✅ MATCHES HTML
                option_a=option_a,
                option_b=option_b,
                option_c=option_c,
                option_d=option_d,
                correct_option=correct_option
            )

            db.session.add(question)
            db.session.commit()

            return redirect("/admin/dashboard")

        return render_template(
            "add_question.html",
            exam=exam
        )

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
