from flask import Flask, render_template, request, url_for, redirect, flash
from flask_login import LoginManager, login_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from users import create_new, username_exist, uid_exist

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bardzo trudny string do zlamania'
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return uid_exist(user_id)


@app.route("/")
@login_required
def index():
    return render_template("index.html",
                           name=current_user.username if current_user.username != "admin" else "li2CTF{4ND_n0_4l4rm5__4nd_N0_54rpr1535}")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = username_exist(username)

    if not user or not check_password_hash(user.password, password):
        flash('NO')
        return redirect(url_for('login'))

    login_user(user, remember=remember)
    return redirect(url_for('index'))


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_post():
    username = request.form.get('username')
    password = request.form.get('password')

    user = create_new(username, generate_password_hash(password, method='sha256'))

    if not user:
        flash('Username already exists')
        return redirect(url_for('signup'))
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=80)
