"""
4a
Napisz program, który po wejściu na adres /planet-details?planet=Tatooine odpowie jsonem zawierającym dane planety,
o którą zapytał użytkownik (np. klimat, liczba mieszkańców). Dane planety program powinien pobierać ze Star Wars API,
np.: https://swapi.co/api/planets/?search=Tatooine
"""


from flask import Flask, request, json, jsonify
import requests
from pprint import pprint


app = Flask(__name__)



@app.route("/planet/<planet>")
def planet_details(planet):
    try:
        resp = requests.get("https://swapi.co/api/planets/?search={}".format(planet))
        resp_json = resp.json()
        results = resp_json["results"][0]
        to_show = json.dumps(results)
        return jsonify(results)
    except IndexError:
        return "No such planet"

if __name__ == '__main__':
    app.run(debug=True)



