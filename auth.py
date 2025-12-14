from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from models import User, db

def init_app(app):

    @app.route("/", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]

            user = User.query.filter_by(email=email).first()

            if user and user.check_password(password):
                login_user(user)
                flash("Login successful!", "success")

                if user.role == "admin":
                    return redirect("/admin/dashboard")
                else:
                    return redirect("/student/dashboard")
            else:
                flash("Invalid email or password", "danger")

        return render_template("login.html")

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            email = request.form["email"]

            if User.query.filter_by(email=email).first():
                flash("Email already registered", "danger")
                return redirect("/register")

            user = User(
                email=email,
                role=request.form["role"]
            )
            user.set_password(request.form["password"])

            db.session.add(user)
            db.session.commit()

            flash("Registration successful! Please login.", "success")
            return redirect(url_for("login"))

        return render_template("register.html")

    @app.route("/logout")
    def logout():
        logout_user()
        flash("You have been logged out", "info")
        return redirect("/")
