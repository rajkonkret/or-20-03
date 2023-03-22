# lambda - odpowiednik funkcji ale w formie krotkiego zapisu
def odejmij(a, b):
    return a - b


odejmij_2 = lambda a, b: a - b
oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100

print(odejmij(4, 2))
print(odejmij_2(4, 2))
print(oblicz_vat(100))

wiek = lambda x: f"dziecko {x}" \
    if x < 10 else \
    (f"nastolatek  {x}" if x < 18 else f"dorosły  {x}")

print(wiek(9))
print(wiek(14))
print(wiek(24))
wiek_2 = 10
print(wiek(wiek_2))
# 13:30
lista = [1, 2, 7, 8, 10, 55]
# zastosowanie funkcji map - mapowanie jednych danych na inne
# f  {} - formatowanie tekstu, w klamerach mozna umiescic wynik dziłania, lub zmienna
# list() - zamiana na liste
print(f"Zastosowanie map: {list(map(lambda x: x * 2, lista))}")
wyn = list(map(lambda x: x * 2, lista))
print(wyn)
print(type(wyn))
# bierze 1 podstawia pod x , wywoluje labde i zwraca wynik - pojedynczy krok
# filter() - filtruje dane
print(f"Zastosowanie filter() {list(filter(lambda x: x < 3, lista))}")
# wyfiltrowac wieksze od 8
# wyfiltrowac wieksze od 3 mniejsze od 20
print(f"Zastosowanie filter() {list(filter(lambda x: x > 8, lista))}")
print(f"Zastosowanie filter() {list(filter(lambda x: 3 < x < 20, lista))}")
