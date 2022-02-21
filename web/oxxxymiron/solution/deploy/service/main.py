from flask import Flask, request, render_template_string, render_template
import requests
import random

app = Flask(__name__)
result_page = open("templates/result.html").read()


@app.route("/result", methods=["POST"])
def result():
    url = request.form['url']
    try:
        resp = requests.get(url, timeout=3)
    except requests.exceptions.ConnectionError:
        return "Connection error!"
    except requests.exceptions.MissingSchema:
        return "Broken url!"
    except requests.exceptions.ReadTimeout:
        return "Timed out!"

    if resp.status_code != 200:
        content = "status_code=" + str(resp.status_code)
    else:
        content = random.choice(resp.text.split())
    print(content)
    res = result_page.format(result=content)
    return render_template_string(res)


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=80)
