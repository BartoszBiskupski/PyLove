from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello you"

@app.route("/witam")
def to_hello():
    return redirect(url_for("hello"))


if __name__ == '__main__':
    app.run(debug=True)