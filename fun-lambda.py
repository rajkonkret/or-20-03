# lambda - odpowiednik funkcji ale w formie krotkiego zapisu
def odejmij(a, b):
    return a - b


odejmij_2 = lambda a, b: a - b
oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100

print(odejmij(4, 2))
print(odejmij_2(4, 2))
print(oblicz_vat(100))

wiek = lambda x: f"dziecko {x}" if x < 10 else (f"nastolatek  {x}" if x < 18 else f"dorosły  {x}")
print(wiek(9))
print(wiek(14))
print(wiek(24))
wiek_2 = 10
print(wiek(wiek_2))
# 13:30
