from math import isqrt
from hashlib import pbkdf2_hmac
from os import urandom


def get_quotes():
    quotes = []
    with open("app/static/quotes.txt", "r") as f:
        for line in f:
            quotes.append(line)
    return quotes


def get_img_urls():
    img_urls = []
    with open("app/static/img_urls.txt", "r") as f:
        for line in f:
            img_urls.append(line)
    return img_urls


def get_bg3_img_urls():
    bg3_img_urls = []
    with open("app/static/bg3_img_urls.txt", "r") as f:
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


def hash_it(password, salt=urandom(16), iters=100000):
    hp = pbkdf2_hmac('sha256', password.encode('utf-8'), salt * 2, iters)
    print("this is the generated salt", salt)
    hp = hp + salt
    print("this is the whole thing", hp)
    return hp


def extract_salt(hashed: bytes, bytes_length=16) -> bytes:
    print("this is the hashed", hashed)
    salt = hashed[-bytes_length:]
    print("salty", salt)
    return salt
