""""Napisz swoją wersję printa o nazwie mojprint, która oprócz zwykłych argumentów pobierze jeszcze obowiązkowo
   ile razy dana rzecz ma być wyprintowana oraz opcjonalnie czy ma być jakiś sufix przed daną wartością. """


def myprint(to_print, print_count=1, prefix=None):
    if prefix:
        added_prefix = str(prefix) +" " + to_print + "\n"
    else:
        added_prefix = to_print
    print(added_prefix * print_count)


class Time:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self):
        return "Time ({} hours, {} minutes, {} seconds)".format(self.h, self.m, self.s)

    def set_time(self, new_h=None, new_m=None, new_s=None):
        if new_h:
            self.h = new_h
        if new_m:
            self.m = new_m
        if new_s:
            self.s = new_s

    def add_time(self, hours=0, minutes=0, sec=0):
        self.h += hours
        self.m += minutes
        self.s += sec
        while self.s > 59:
            self.m += 1
            self.s -= 60
        while self.m > 59:
            self.h += 1
            self.m -= 60
        while self.h > 23:
            self.h -= 24

    def get_seconds(self):
        return "{} equals to {} seconds.".format(self.__str__(), (self.h * 3600 + self.m * 60 + self.s))

    def get_minutes(self):
        return "{} equals to {} minutes.".format(self.__str__(), ((self.h * 60 + self.m) + round(self.s/60, 2)))

    def get_hours(self):
        return "{} equals to {} hours.".format(self.__str__(), (self.h + (round(self.m/60, 2) + round(self.s/3600, 3))))


"""Stwórz klasę Zegar, która dziedziczy po Czas a konstruktor (__init__) 
będzie brał obowiązkowo parametr format (12H lub 24H) oprócz tych co Czas. """


class Clock(Time):
    def __init__(self, time_format, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.time_format = time_format


"""Stwórz klasę DokładnyZegar, która dziedziczy po Zegar i która jeszcze będzie przyjmowała opcjonalnie milisekundy."""


class PreciseClock(Clock):
    def __init__(self, *args, ms=0, **kwargs):
        super().__init__(*args, **kwargs)
        self.ms = ms


time = Time(23, 59, 50)
time.add_time(hours=10, sec=40)

print(time.get_hours())