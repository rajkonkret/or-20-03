class Human:
    """
    Klasa opisująca człowieka w Pythonie
    """

    # włąsny konstruktor klasy
    def __init__(self, imie, wiek=39, plec='k'):
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

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


cz_1 = Human("Radek", 48, "m")
print(cz_1.imie)
cz_1.powitanie()

