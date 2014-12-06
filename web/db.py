from coaster.sqlalchemy import TimestampMixin
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres@db/flask_app"
db = SQLAlchemy(app)

class Tick(TimestampMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
