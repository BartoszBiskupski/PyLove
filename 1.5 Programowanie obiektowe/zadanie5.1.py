class Human:
    bmi = 0
    kilo = 6000

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def speak(self):
        print("I tell the truth")

    def count_bmi(self):
        self.height = self.height / 100
        self.bmi = self.weight / self.height ** 2
        return "Your BMI is {}.".format(round(self.bmi, 2))

    def diff_to_norm(self):
        if self.bmi < 18.5:
            expected_weight = 18.5 * (self.height ** 2)
            diff = round(expected_weight - self.weight, 2)
            print("You need to gain {}".format(diff))
        elif self.bmi > 25:
            expected_weight = 25 * (self.height ** 2)
            diff = round(self.weight - expected_weight, 2)
            print("You need to lose {}".format(diff))
        else:
            diff = 0
            print("You are fine")

    """
    Zakładając, że aby schudnąć 1 kg trzeba spalić 6000kcal, napisz funkcjonalność, która powie użytkownikowi,
    ile powinien godzin biegać(500kcal/h) / jeździć rowerem(600kcal/h) / uprawiać hobby(250kcal/h) / 
    grać w szachy(150kcal/h) / etc. aby być w normie (to_burn).
    """
    def running(self):
        if self.count_bmi() < 25:
            print("You don't need to run")
        else:
            kcal_tolose = self.count_bmi() * self.kilo



class Politician(Human):
    bribe = False

    def speak(self):
        if self.bribe:
            super().speak()
        else:
            print("I lie cuz I can")

    def accept_bribe(self):
        self.bribe = True


human = Human("Ziutek", 178, 76)
politician = Politician("Bleh", 180, 100)
human.count_bmi()
human.diff_to_norm()
