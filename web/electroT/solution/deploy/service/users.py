import psycopg2
import random

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

conn = psycopg2.connect("postgresql://polvouser:polvo228@psql:5432/polvodb")

cur = conn.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS users(uid varchar(1024) PRIMARY KEY, username varchar(255), password varchar(255));")

conn.commit()


class User(UserMixin):
    def __init__(self, uid, username, password):
        self.uid = uid
        self.username = username
        self.password = password

    def get_id(self):
        return str(self.uid)


def get_uid():
    uid = random.randint(0, 10 ** 1000)
    while uid_exist(uid):
        uid = random.randint(0, 10 ** 1000)
    return uid


def uid_exist(uid):
    cur.execute(f"SELECT uid, username, password FROM users WHERE uid = '{str(uid)}'")
    arr = cur.fetchall()
    if not arr:
        return None
    arr = arr[0]
    return User(*arr)


def username_exist(username):
    cur.execute(f"SELECT uid, username, password FROM users WHERE username = (%s)", (username,))
    arr = cur.fetchall()
    if not arr:
        return None
    arr = arr[0]
    return User(*arr)


def credentials_exist(username, password):
    cur.execute("SELECT uid, username, password FROM users WHERE username = (%s) AND password = (%s)",
                (username, password))
    arr = cur.fetchall()
    if not arr:
        return None
    arr = arr[0]
    return User(*arr)


def create_new(username, password):
    uid = get_uid()
    print(uid)
    if not username_exist(username):
        cur.execute("INSERT INTO users VALUES (%s, %s, %s)", (uid, username, password))
        conn.commit()
        return User(uid, username, password)


create_new("admin", generate_password_hash("ysdklc832784jdf", method='sha256'))
