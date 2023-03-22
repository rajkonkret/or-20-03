from abc import ABC, abstractmethod


class Ptak(ABC):
    """"
    klasa opisujaca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lataj(self):
        print("Tu", self.gatunek, "Lece z szybkoscia", self.szybkosc)

    @abstractmethod     # metoda abstrakcyjna - nie mozna wywołac bez nadpisania w klasach dziedziczacych
    def wydaj_odglos(self):
        pass


class Orzel(Ptak):
    """
    to jest orzeł
    """

    def poluj(self):
        print("Tu", self.gatunek, "Zaczynam polowanie")

    def wydaj_odglos(self):
        print("piiiiiii")


class Kura(Ptak):

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)
        self.gatunek = gatunek

    def lataj(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("kokokokok")


# orzel = Ptak("orzel", 10)
# orzel.wydaj_odglos()
# orzel.lataj()
# kura = Ptak("kura", 0)
# kura.lataj()
orzel_2 = Orzel("orzel", 10)
orzel_2.lataj()
kura_2 = Kura("kura")
kura_2.lataj()
orzel_2.poluj()
orzel_2.wydaj_odglos()
kura_2.wydaj_odglos()
