from flask import Flask
from flask_wtf import CSRFProtect
import secrets
import helper


def create_app():
    flaskapp = Flask(__name__)
    return flaskapp


app = create_app()
quotes_list = helper.get_quotes()
img_urls = helper.get_img_urls()
bg3_img_urls = helper.get_bg3_img_urls()

csrf = CSRFProtect(app)
foo = secrets.token_urlsafe(16)
app.config["SECRET_KEY"] = foo
app.secret_key = foo

import routes

if __name__ == "__main__":
    app.run(debug=True)