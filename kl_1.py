# klasa - szablon wg ktorego zbudujemy obiekt klasy

class Human:
    """
    To jest klasa opisujaca człowieka w Pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):  # podstaw obiekt co mnie wywołał
        """
        metoda witajaca
        :return:
        """
        print("Nazywam się", self.imie)

    # self.imie - uzycie wartosci pola imie z obektu
    # dodac w klasie metode ruszaj. mezczyzna mowi Ruszyłem, kobieta Ruszyłam

    def ruszaj(self):
        if self.plec == 'k':
            print("Ruszyłam w droge")
        else:
            print("Ruszyłem w droge")


# wyswietlenie dokumentacji klasy
print(Human.__doc__)
# budowanie obiektu klasy Human
# obiekty z małej litery
cz_1 = Human()
print(cz_1)
print(cz_1.plec)
print(cz_1.imie)
print(cz_1.wiek)
cz_1.imie = "Radek"
cz_1.wiek = 39
cz_1.plec = "m"
print(cz_1.plec)
print(cz_1.imie)
print(cz_1.wiek)
cz_1.powitanie()  # wywołanie bez self
cz_1.ruszaj()
