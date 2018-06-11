"""
Napisz aplikację, która po wejściu na adres "/konto" wyświetli stan konta użytkownika i listę ostatnich przelewów.
Początkowy stan konta ustaw np. na 1000 zł. Na stronie powinien znajdować się formularz, umożliwiający wykonanie
przelewu - powinien zawierać dwa pola tekstowe: * nr konta docelowego, * kwotę przelewu. Po przesłaniu formularza
kwota na koncie powinna zostać zmniejszona o podaną wartość, ponadto nowy przelew powinien pojawić się na liście
ostatnich przelewów. Upewnij się, że odświeżenie strony po wykonaniu przelewu nie spowoduje wykonania tego przelewu
jeszcze raz.
"""

from flask import Flask, request, render_template, redirect, url_for
import datetime

app = Flask(__name__)

account = {"balance": 1000.00,
           "history": []
           }

@app.route("/")
def to_index():
    return redirect(url_for("balance"))


@app.route("/user")
def to_index():
    return redirect(url_for("balance"))


@app.route("/account", methods=["GET", "POST"])
def balance():
    global account
    bal = account["balance"]
    if request.method == "POST":
        bank_account = request.form.get("bank_account")
        amount = float(request.form.get("amount"))
        account["balance"] -= amount
        account["history"].append([datetime.datetime.now(), bank_account, amount])
        return redirect(url_for("balance", balance=bal, history=account["history"]))
    else:
        balance = account["balance"]
        return render_template("index.html", balance=balance, history=account["history"])


if __name__ == '__main__':
    app.run(debug=True)