tuple_1 = ("Tomek", "ASia", "Marek", "Paulina")
tuple_2 = ("Radek",)  # tupla jednoelementowa, zmienna, niezmienna
tuple_3 = (43, 55, 22.42, 11, 200)

print(tuple_1)
print(tuple_2)
print(type(tuple_2))
print(type(tuple_3))
# wyswietlic tuple_3
print(tuple_3)
print(tuple_1.count("Tomek"))
print(tuple_1.index("Tomek"))

name = tuple_1[0]
print(name)
print(len(tuple_1))

# deklaracja [], ()
# odczyt po indexie []

a, b, *c = 1, 2, 3, 4
print(a)
print(b)
print(c)

tuple_1 = ("Tomek", "ASia", "Marek", "Paulina")

imie_1, *imie_2, imie_3 = tuple_1  # rozpakowanie tupli
print(imie_1)
print(imie_2)
print(imie_3)
print(tuple_1)

lista = list(tuple_1)  # zamiana tupli na liste
print(lista)
