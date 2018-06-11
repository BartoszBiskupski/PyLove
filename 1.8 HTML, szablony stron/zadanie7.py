"""
Napisz aplikację, która wyświetla stronę HTML zawierającą listę zespołów (zdefiniowaną w aplikacji) oraz formularz
do wyszukiwania z jednym inputem. Przesłanie formularza powinno spowodować wyświetlenie tylko tych zespołów,
które w nazwie zawierają ciąg znaków podany przez użytkownika.
"""

from flask import Flask, render_template, request

app = Flask(__name__)

bands = ["Tool", "Metallica", "Daft Punk", "Moderat"]


@app.route("/bands")
def index():
    query = request.args.get("bands")
    if query:
        search_results = [b for b in bands if query.lower() in b.lower()]
    else:
        search_results = bands
    return render_template("index.html", search_results=search_results)


if __name__ == '__main__':
    app.run(debug=True)