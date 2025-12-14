from flask import Flask
from config import Config
from models import db, User
from flask_login import LoginManager

import auth
import admin
import student

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# register routes
auth.init_app(app)
admin.init_app(app)
student.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
