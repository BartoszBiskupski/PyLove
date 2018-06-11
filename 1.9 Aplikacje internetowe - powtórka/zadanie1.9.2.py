"""Napisz aplikację, która będzie wyświetlać dane pracowników pewnej firmy. Każdy pracownik będzie mieć identyfikator,
imię, nazwisko, płacę, opis stanowiska (użyj klasy po stronie serwera). Utwórz stonę zawierającą tabelę pracowników
(adres wymyśl samodzielnie). W każdym wierszu tabeli powinny znaleźć się imię, nazwisko pracownika i dodatkowa pusta
komórka - uzupełnimy ją w następnym zadaniu. """

from flask import Flask, request, render_template, redirect, url_for
import datetime

app = Flask(__name__)


class Employee:
    def __init__(self, ide, name, last_name, salary, role):
        self.ide = ide
        self.name = name
        self.last_name = last_name
        self.salary = salary
        self.role = role


employee1 = Employee(1, "Bruce", "Wayne", 50000, "Batman")
employee2 = Employee(2, "Clark", "Kent", 5, "Superman")
employees = [employee1, employee2]


@app.route("/")
def to_index():
    return redirect(url_for("show_employees"))

@app.route("/employees")
def show_employees():
    global employees
    list_of_details = []
    for emp in employees:
        list_of_details.append([v for k, v in vars(emp).items()])
    return render_template("index_emp.html", list_of_details=list_of_details)

@app.route("/employees/<int:id>")
def details(id):
    global employees
    details = [v for k, v in vars(employees[id-1]).items()]
    return render_template("em_details.html", details=details)

@app.route("/add" methods=["POST", "GET"])
def add_e():
    if request.method == "POST":
        new_empl = Employee(
            idrequest.form.get
        )

if __name__ == '__main__':
    app.run(debug=True)