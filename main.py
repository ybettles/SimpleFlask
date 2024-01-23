from flask import Flask, current_app, url_for, render_template
from time import time, ctime
from random import randint
from math import isqrt

def get_quotes():
    quotes = []
    with open("static/quotes.txt", "r") as f:
        for line in f:
            quotes.append(line)
    return quotes

def get_img_urls():
    img_urls = []
    with open("static/img_urls.txt", "r") as f:
        for line in f:
            img_urls.append(line)
    return img_urls

def get_bg3_img_urls():
    bg3_img_urls = []
    with open("static/bg3_img_urls.txt", "r") as f:
        for line in f:
            bg3_img_urls.append(line)
    return bg3_img_urls
def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
def create_app():
    flaskapp = Flask(__name__)
    return flaskapp

app = create_app()
quotes_list = get_quotes()
img_urls = get_img_urls()
bg3_img_urls = get_bg3_img_urls()

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
