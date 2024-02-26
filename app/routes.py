from app.helper import is_prime, get_img_urls, get_bg3_img_urls, get_quotes, hash_it, extract_salt
from app import app, db
from app import forms
from app.models import User, Item
from flask import current_app, url_for, render_template, redirect, flash, make_response, request
from time import time, ctime
from random import randint


# ----------
# Index Page
# ----------
@app.route("/")
def home():
    return render_template('home.html', title="Home")


# ------------
# Current Time
# ------------
@app.route("/current-time")
def current_time():
    t = time()

    return ctime(t)


# -------------
# Random Quotes
# -------------
@app.route("/quotes")
def quotes():
    q = get_quotes()
    i = randint(0, len(q))

    return render_template('quotes.html', quote=q[i], title="Quote")


# -----------
# View Config
# -----------
@app.route("/view-config")
def view():
    name = current_app.name
    config = current_app.config

    return render_template('view.html', name=name, config=config, title="Config")


# ----------------
# Prime Check Form
# ----------------
@app.route("/primality-check", methods=['GET', 'POST'])
def primePage():
    form = forms.NumberForm()
    message = ""
    number = 0

    if form.validate_on_submit():
        number = form.numberField.data
        return redirect(url_for('prime', number=number), code=302)
    else:
        print(form.errors)
        message = "Invalid input, please try again."

    return render_template('prime-page.html', title="Primality Check", form=form, message=message)


# -----------------------
# Prime Check Result Page
# -----------------------
@app.route("/primality-check/int=<int:number>")
def prime(number):
    isPrime = is_prime(number)

    return render_template('prime.html', isPrime=isPrime, number=number, title=str(number))


# --------------
# Ori Image Page
# --------------
@app.route("/ori")
def ori():
    imgs = get_img_urls()
    i = randint(0, len(imgs)-1)

    return render_template('ori.html', img_url=imgs[i], title="Ori Page")


# -----------------------
# Baldurs Gate Image Page
# -----------------------
@app.route("/bg3")
def bg3():
    urls = get_bg3_img_urls()
    i = randint(0, len(urls)-1)

    return render_template('bg3.html', bg3_img_url=urls[i], title="BG3 Image Dump")


# ------------
# Sign Up Page
# ------------
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = forms.SignUpForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        print(username)
        print(password)

        hp = hash_it(password)
        user = User(username=username, hashedpassword=hp)
        db.session.add(user)

        try:
            db.session.commit()
            flash("New user added with username:" + username)
            return redirect(url_for('home'), code=302)
        except:
            db.session.rollback()
            print("db changes rolled back")
            if User.query.filter_by(username=username).first():
                form.username.errors.append('This username is taken, please choose a different one and try again.')

    else:
        print(form.errors)
        message = "Invalid input, please try again."
    return render_template('signup.html', form=form, title="Sign Up")


# ----------
# Login Page
# ----------
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # get hash corresponding to that username (if username exists)
        stored_hash = db.session.query(User.hashedpassword).filter_by(username=username).first()[0]
        # get salt from stored hash
        salt = extract_salt(stored_hash)
        # hash the password given using the same salt
        correct = hash_it(password, salt=salt) == stored_hash
        # see if match - if it's true, u can log in wahoo, if no, booooo get out
        if correct:
            # ur details were good, you're logged in, make cookies
            resp = make_response("Logging you in")
            resp.set_cookie("username", username)

            return render_template('landingpage.html', title=(username + "'s Page"), username=username, response=resp)
        else:
            # ur details are bad, try again
            form.form_errors.append('Incorrect username or password. Please try again.')

    return render_template('login.html', form=form, title="Login")

@app.route("/landingpage")
def landing():
    try:
        current_user = request.cookies.get('username')
        return render_template('landingpage.html', title=(current_user+"'s Page"), username=current_user)
    except:
        return redirect(url_for('login'), code=302)

