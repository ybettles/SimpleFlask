import os

from flask import Flask
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

import secrets


def create_app():
    app = Flask(__name__)
    # with app.app_context():
    # intialise db here
    # manually adding the db: go to terminal, type in flask shell, and then type in db.create_all()
    return app


app = create_app()

csrf = CSRFProtect(app)
foo = secrets.token_urlsafe(16)
app.config["SECRET_KEY"] = foo
app.secret_key = foo

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data', 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

"""
if __name__ == "__main__":
    app.run(debug=True)
"""

# TODO: in here i need an "if db doesnt exist, create it"

from app import routes
from app.models import *


@app.shell_context_processor
def make_shell_context():
    return dict(db=db)
