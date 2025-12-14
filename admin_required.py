from flask_login import current_user
from flask import redirect, url_for, flash
from functools import wraps

def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            flash("Please login first", "warning")
            return redirect(url_for("login"))

        if current_user.role != "admin":
            flash("Access denied: Admins only", "danger")
            return redirect("/student/dashboard")

        return func(*args, **kwargs)
    return wrapper
