from flask import Flask, url_for, request, render_template, make_response
import base64

# credits of css template go to https://www.free-css.com/free-css-templates/page256/it-next

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    print("[*] Server is ready!")
    app.run(host="0.0.0.0", port=21013)
