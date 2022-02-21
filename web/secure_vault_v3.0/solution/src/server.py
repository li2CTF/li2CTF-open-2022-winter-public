from flask import Flask, url_for, request, render_template
from flask_wtf import FlaskForm
import wtforms
import threading
from reinit_db import reinit
import random
import sqlite3
from string import ascii_letters


DATABASE_NAME = "vault.db"
ALPH = ascii_letters + "0123456789"


def random_key() -> str:
    data = []
    for i in range(random.randint(12, 30)):
        data.append(random.choice(ALPH))
    return "".join(data)


app = Flask(__name__)
app.config["SECRET_KEY"] = random_key()
app.config["WTF_CSRF_CHECK_DEFAULT"] = False
app.config["WTF_CSRF_ENABLED"] = False


def timer_reinit():
    threading.Timer(240.0, timer_reinit).start()
    print("[.] Reinited db")
    reinit()


class LoginForm(FlaskForm):
    username = wtforms.StringField("Username", validators=[wtforms.validators.DataRequired()])
    password = wtforms.PasswordField("Password", validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("Login")


def check_username(username):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    try:
        c.execute("SELECT username FROM users WHERE username=(?)", (username,))
    except Exception as e:
        return False
    if c.fetchone():
        return True
    return False


def check_password(username, password):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    try:
        c.execute(f"SELECT password FROM users WHERE username=(?) and password=(?)", (username, password,))
    except Exception as e:
        print(e)
        return False
    if c.fetchone():
        return True
    return False

def get_data(username, password):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    try:
        c.execute(f"SELECT data FROM users WHERE username=(?) and password=(?)", (username, password,))
    except Exception as e:
        print(e)
        return False
    q = c.fetchone()[0]
    return q


@app.route("/", methods=["GET", "POST"])
def index():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        if not check_username(form.username.data):
            return render_template("index.html", form=form, error="Incorrect username or password.")
        if not check_password(form.username.data, form.password.data):
            return render_template("index.html", form=form, error="Incorrect username or password.")
        user_data = get_data(form.username.data, form.password.data)
        print(f"[!] Entered admin storage with password={form.password.data}")
        return render_template("vault.html", data=user_data)
    return render_template("index.html", form=form)


if __name__ == "__main__":
    print("[*] Server is ready!")
    timer_reinit()
    app.run(host="0.0.0.0", port=21010)
    