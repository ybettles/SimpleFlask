import os
from flask import Flask
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
import secrets
from app import helper


app = Flask(__name__)
quotes_list = helper.get_quotes()
img_urls = helper.get_img_urls()
bg3_img_urls = helper.get_bg3_img_urls()

csrf = CSRFProtect(app)
foo = secrets.token_urlsafe(16)
app.config["SECRET_KEY"] = foo
app.secret_key = foo
basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy(app)

"""
if __name__ == "__main__":
    app.run(debug=True)
"""

from app import routes
from app.models import *
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Student=Student, Loan=Loan, datetime=datetime)