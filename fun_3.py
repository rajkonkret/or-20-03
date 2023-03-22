a = 10  # zminna globalna a


def dodaj():
    a = 4  # zmienne lokalne
    b = 10
    print("Wynik", a + b)


def dodaj_2():
    global a  # a lokalne staje sie globalne, zostaje nadpisane globalnie
    a = 4   # nadpisanie zmiennej globalnej
    b = 10
    print("Wynik", a + b)


# wartos a z gory przed wykonaniem funkcji dodaj()
print("Wartosc a z góry(globalnej", a)  # a  = 10
# wywołanie dodaj, ale dodaj ma a lokalne, nie nadpisze
dodaj()  # tam a = 4
# a z gory(globalna) nadal ma 10
print("Wartoc a z gory(globalnej)", a)  # a = 10 ?
# wywołujemy dodaj_2, ale dodaj_2 uzywa zmiennej globalne a, nadpisze a z gory
dodaj_2()
# a zostało nadpisane i wynosi teraz 4
print("Wartoc a z gory(globalnej)", a)  # a =
