"""
(Do domu) ...po wejściu na /user/<username>/login aplikacja powinna zwracać token w formacie UUID4.
"""

from flask import Flask, request
import requests

app = Flask(__name__)


@app.route("/user/<username>/login")
def token(username):
    token = requests.get("https://www.uuidgenerator.net/api/version4")
    token_text = token.text
    return "Token for {}: {}.".format(username, token_text)


if __name__ == '__main__':
    app.run(debug=True)