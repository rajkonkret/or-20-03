dict = {}  # pusty słownik
slownik = {'name': 'Radek', 'nazwisko': 'Kowalski'}

print(slownik)

# wypisanie kluczy
for k in slownik:
    print(k)

# wypisanie wartosci
for v in slownik.values():
    print(v)

# wypisanie kluczy sposób 2
for k in slownik.keys():
    print(k)

# wypisanie itemów
for k, v in slownik.items():
    print(k, '=>', v)
# stworzyc dowolny słownik, wypisac do wyboru: klucze, wartosci, itemy
# ---
slownik = {'name': ['Radek', 'Tomek'], 'nazwisko': ['Kowalski', 'Nowak']}
for k, v in slownik.items():
    print(k, "=>", v)

slownik_2 = {'name': 'Radek', 'nazwisko': 'Kowalski', 'wiek': 44}

for k, v in slownik_2.items():
    print(k, "=>", v)

# petla for od liczby ujemnej
for i in range(-10, 1):
    print(i)

# petla z krokiem 2, 0 - poczatek, 10 - koniec(0..9), 2 - krok
for i in range(0, 10, 2):
    print(i)

#  petla do tyłu
for i in range(10, -10, -1):
    print(i)
