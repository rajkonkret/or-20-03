a = 6
b = 7
cena = 100


# funkcja dodaj() zwracajaca wynik
def dodaj():
    return a + b


# funkcja z argumentami
def dodaj_2(a, b):
    """
    Zwraca wynik dodawania
    :param a:
    :param b:
    :return:  wynik dodawania
    """
    return a + b


# zrobic funkcje odejmowanie() mnozenie()
def mnozenie(a, b, c=1):
    return a * b * c


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


wyn = dodaj()
print(wyn)
# wywoła sie dodaj - zwroci wynik 13, nastepnie wywolujemy dodaj_2(13- wynik metody dodaj(),7)
print(dodaj_2(dodaj(), 7))
print(mnozenie(2, 3))
print(mnozenie(2, 3, 4))

# wywołanie z kwota 100 zł, vat domyslny 23
print(oblicz_vat(100))
# wywołanie z kwota 100 zł, vat 8
print(oblicz_vat(100, 8))
# wywołanie z kwota ze zmiennej globalnej cena (100)
print(oblicz_vat(cena))
