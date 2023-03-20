wiek = 47  # int
rok = 2023  # int
temp = 36.6  # float - zmiennoprzecinkowy
print(0.2 + 0.7)

# wypisac zawartosc tych zmiennych
print(wiek)
print(rok)
print(temp)

print(wiek * rok)
print(wiek - rok)
print(wiek + rok)
print(wiek / rok)
print(type(wiek / rok))  # wyniku float
print(wiek // rok)  # czesc całkowita z dzielenia
print(type(wiek // rok))  # czesc całkowita z dzielenia - int
print(4 / 2)
print(wiek ** rok)  # potegowanie
print(54 - (5 * 43) + (4 / 2 + 4) / 2)
# eval

print("Sprawdzam zmienna temp {} {} {}".format(wiek, temp, ''))
print(f"\tSprawdzam zmienna temp {wiek} {temp}\n")

print(f"""
    {wiek}
    {temp}
""")

imie = "Radek Radek"
print(imie)
print(imie.lower())  # zamiana na małe litery
print(imie.capitalize())  # pierwsza litera z duzej
print(imie.count("a"))

czy_znasz_Pythona = False  # fałsz
czy_znasz_Pythona = True  # prawda
print(czy_znasz_Pythona)
print(type(czy_znasz_Pythona))
print(int(czy_znasz_Pythona))  # 1 - prawda, 0 - fałsz
print(bool(1))  # rzutowanie int na bool
