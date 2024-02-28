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
    """
    Checks whether the integer input is a prime number or not.
    :param n: int - number to check
    :return: boolean - True if n is prime, False otherwise.
    """
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
    """
    Hashes password using repeated SHA256 with salt
    - salt can be given as a keyword parameter, if not will be generated (16 bytes in length).
    :param password: str - the password string to be hashed
    :param salt: bytes - the salt to use in the hashing algorithm.
                    if not specified, will generate a random 16 byte sequence.
    :param iters: int - number of iteration to perform in the hashing algorithm.
    :return: bytes - the hashed password concatenated with the salt that was used.
    """
    hp = pbkdf2_hmac('sha256', password.encode('utf-8'), salt * 2, iters)
    hp = hp + salt
    return hp


def extract_salt(hashed: bytes, bytes_length=16) -> bytes:
    """
    Slices a bytes object to obtain a partition at the end of it.
    Used to take the salt out of the concatenated bytes of hash and salt.
    :param hashed: bytes - the concatenated bytes objet to extract the salt from the end of.
    :param bytes_length: int - length of salt in bytes. defaults to 16.
    :return: bytes - salt as extracted from the concatenated bytes object.
    """
    salt = hashed[-bytes_length:]
    return salt
