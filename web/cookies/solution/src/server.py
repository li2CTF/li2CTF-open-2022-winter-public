from flask import Flask, url_for, request, render_template, make_response
import base64

# credits of css template go to https://www.free-css.com/free-css-templates/page256/it-next

FLAG_COOKIES = "li2CTF{4ll_7h3_c0d3rz_l0v3_c00k135__d0n7_7h3y?}"
FLAG_ROBOTS = "li2CTF{b33p_b00p__0lvl_ch4ll3ng3_s0lv3d}"
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    resp = make_response(render_template('index.html'))
    if not request.cookies.get('secret'):
        resp.set_cookie('secret', base64.b64encode(FLAG_COOKIES.encode()))
    return resp


@app.route("/robots.txt", methods=["GET"])
def robots():
    resp = make_response(FLAG_ROBOTS)
    if not request.cookies.get('secret'):
        resp.set_cookie('secret', base64.b64encode(FLAG_COOKIES.encode()))
    return resp


if __name__ == "__main__":
    print("[*] Server is ready!")
    app.run(host="0.0.0.0", port=21012)
