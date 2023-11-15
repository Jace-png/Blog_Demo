import secrets
import string
import hashlib


def generate_secret_key(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    secret_key = ''.join(secrets.choice(alphabet) for _ in range(length))
    return secret_key


def gen_md5(text):
    md5 = hashlib.md5()
    md5.update(text.encode('utf8'))
    return md5.hexdigest()
