from helper import is_prime
from main import app, quotes_list, img_urls, bg3_img_urls
from flask import current_app, url_for, render_template, redirect
from time import time, ctime
from random import randint

import numberForm
import signUpForm


@app.route("/")
def home():
    return render_template('home.html', title="Home")


@app.route("/current-time")
def current_time():
    t = time()
    return ctime(t)


@app.route("/quotes")
def quotes():
    i = randint(0, len(quotes_list))
    return render_template('quotes.html', quote=quotes_list[i], title="Quote")


@app.route("/view")
def view():
    name = current_app.name
    config = current_app.config
    return render_template('view.html', name=name, config=config, title="Config")


@app.route("/primality-check", methods=['GET', 'POST'])
def primePage():
    form = numberForm.NumberForm()
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
    i = randint(0, len(img_urls)-1)
    return render_template('ori.html', img_url=img_urls[i], title="Ori Page")


@app.route("/bg3")
def bg3():
    i = randint(0, len(bg3_img_urls)-1)
    return render_template('bg3.html', bg3_img_url=bg3_img_urls[i], title="BG3 Image Dump")


@app.route("/signup")
def signup():
    signUp = signUpForm.SignUpForm()
    return render_template('signup.html', form=signUp, title="Sign Up")



