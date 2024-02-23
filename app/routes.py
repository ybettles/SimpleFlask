from app.helper import is_prime, get_img_urls, get_bg3_img_urls, get_quotes
from app import app, db
from flask import current_app, url_for, render_template, redirect
from time import time, ctime
from random import randint

from app import forms


@app.route("/")
def home():
    return render_template('home.html', title="Home")


@app.route("/current-time")
def current_time():
    t = time()
    return ctime(t)


@app.route("/quotes")
def quotes():
    q = get_quotes()
    i = randint(0, len(q))
    return render_template('quotes.html', quote=q[i], title="Quote")


@app.route("/view")
def view():
    name = current_app.name
    config = current_app.config
    return render_template('view.html', name=name, config=config, title="Config")


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


@app.route("/primality-check/int=<int:number>")
def prime(number):
    isPrime = is_prime(number)
    return render_template('prime.html', isPrime=isPrime, number=number, title=str(number))


@app.route("/ori")
def ori():
    imgs = get_img_urls()
    i = randint(0, len(imgs)-1)
    return render_template('ori.html', img_url=imgs[i], title="Ori Page")


@app.route("/bg3")
def bg3():
    bg3 = get_bg3_img_urls()
    i = randint(0, len(bg3)-1)
    return render_template('bg3.html', bg3_img_url=bg3[i], title="BG3 Image Dump")


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    signUp = forms.SignUpForm()
    return render_template('signup.html', form=signUp, title="Sign Up")



