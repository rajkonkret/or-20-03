# funkcja
a = 1
b = 7


# definicja funkcji bezargumentowej
# te funkcje nic nie zwracaja po wykonaniu
def dodaj():
    print(a + b)


def dodaj_2(a, b):
    print(a + b)


def odejmij(a, b, c=0):
    print(a - b - c)


# wywołnie funkcji
dodaj()
dodaj_2(5, 4)
odejmij(1, 2)
odejmij(1, 2, 3)
odejmij(b=1, a=2, c=3)  # podanie argumentów poprzez nazwe
