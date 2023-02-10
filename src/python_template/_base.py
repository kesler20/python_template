from datetime import timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


# SERVER SIDE APPLICATION
app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///python_template.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "top secret!"
app.permanent_session_lifetime = timedelta(minutes=50)

# DATABASE API
db = SQLAlchemy(app)
