class Human:
    bmi = 0
    kilo = 6000
    exercise ={
        "running": kilo/500,
        "riding": kilo/600,
        "hobby": kilo/250,
        "chess": kilo/150,
    }
    food ={
        "chocolate": kilo/4500,
        "potatoes": kilo/800
    }

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def speak(self):
        return "I tell the truth"

    def count_bmi(self):
        self.height = self.height / 100
        self.bmi = self.weight / self.height ** 2
        return "Your BMI is {}.".format(round(self.bmi, 2))

    def diff_to_norm(self):
        if self.bmi < 18.5:
            expected_weight = 18.5 * (self.height ** 2)
            diff = round(expected_weight - self.weight, 2)
            return "You need to gain {}".format(diff)
        elif self.bmi > 25:
            expected_weight = 25 * (self.height ** 2)
            diff = round(self.weight - expected_weight, 2)
            return "You need to lose {}".format(diff)
        else:
            return "You are fine"

    """
    Zakładając, że aby schudnąć 1 kg trzeba spalić 6000kcal, napisz funkcjonalność, która powie użytkownikowi,
    ile powinien godzin biegać(500kcal/h) / jeździć rowerem(600kcal/h) / uprawiać hobby(250kcal/h) / 
    grać w szachy(150kcal/h) / etc. aby być w normie (to_burn).
    """

    def exercises(self):
        diff_bmi = round(self.bmi - 25, 2)

        if diff_bmi > 0:
            return """To lose {d} kilos you need to: 
            - {r} hours of running 
            - {b} hours of riding on a bicycle 
            - {h} hours of doing your hobby 
            - {c} hours to play chess""".format(d=diff_bmi,
                                                r=self.exercise["running"]*diff_bmi,
                                                b=self.exercise["riding"]*diff_bmi,
                                                h=self.exercise["hobby"]*diff_bmi,
                                                c=self.exercise["chess"]*diff_bmi
                                                )
        else:
            return "You don't need to exercise, eat a donut"


    """Zakładając, że aby przytyć 1 kg trzeba dostarczyć 6000kcal, napisz funkcjonalność, która powie użytkownikowi, 
    ile powinien zjeść czekolady(450kcal/100g) / ziemniaków(80kcal/100g) więcej aby być w normie (to_eat) """

    def gain_weight(self):
        diff_bmi = round(18.5 - self.bmi, 2)
        if diff_bmi > 0:
            return """"To gain {d} kilos you need to eat:
            - {c} kilos of chocolate,
            - {p} kilos of potatoes""".format(d=diff_bmi,
                                              c=self.food["chocolate"]*diff_bmi,
                                              p=self.food["potatoes"]*diff_bmi
                                              )

    def what_to_do(self):
        if self.bmi < 18.5:
            return self.gain_weight()
        elif self.bmi > 25:
            return self.exercises()


class Politician(Human):
    bribe = False

    def speak(self):
        if self.bribe:
            super().speak()
        else:
            print("I lie cuz I can")

    def accept_bribe(self):
        self.bribe = True


human = Human("Ziutek", 178, 150)
politician = Politician("Bleh", 180, 50)
human.count_bmi()
politician.count_bmi()
print(human.what_to_do())
print(politician.what_to_do())
