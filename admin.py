from flask import render_template, request, redirect, flash
from flask_login import login_required
from admin_required import admin_required
from models import Exam, Question, db

def init_app(app):

    @app.route("/admin/dashboard")
    @login_required
    @admin_required
    def admin_dashboard():
        exams = Exam.query.all()
        return render_template("admin_dashboard.html", exams=exams)

    @app.route("/admin/create-exam", methods=["GET", "POST"])
    @login_required
    @admin_required
    def create_exam():
        if request.method == "POST":
            exam = Exam(
                title=request.form["title"],
                description=request.form["description"],
                duration=int(request.form["duration"])
            )
            db.session.add(exam)
            db.session.commit()
            flash("Exam created successfully", "success")
            return redirect("/admin/dashboard")

        return render_template("create_exam.html")

    @app.route("/admin/add-question/<int:exam_id>", methods=["GET", "POST"])
    @login_required
    @admin_required
    def add_question(exam_id):
        if request.method == "POST":
            q = Question(
                exam_id=exam_id,
                question_text=request.form["question_text"],
                option_a=request.form["option_a"],
                option_b=request.form["option_b"],
                option_c=request.form["option_c"],
                option_d=request.form["option_d"],
                correct_option=request.form["correct_option"]
            )
            db.session.add(q)
            db.session.commit()
            flash("Question added", "success")
            return redirect("/admin/dashboard")

        return render_template("add_question.html")
