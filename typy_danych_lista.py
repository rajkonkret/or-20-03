lista = []  # deklaracja pustej listy
lista_2 = []
print(lista)
print(type(lista))
lista.append("Radek")
lista.append("Maciek")
lista.append("Tomek")
lista.append("Paulina")

print(lista)
print(lista[1])
print(lista[0], lista[-2])
lista.insert(1, "Piotr")  # wstawienie elementu pomiedzy index 0 i 1
print(lista)
lista[2] = "Krzysztof"  # nadpisanie elementu na indeksie 2
print(lista)
lista.remove("Tomek")
print(lista)
lista_2.append(lista.pop(2))  # usuniecie po indeksie i zapisanie do drugiej listy
print(lista)
print(lista_2)
print(lista + lista_2)
lista_3 = lista.copy()  # kopiuje liste do nowej
lista.clear()  # czysci liste(zeruje)
print(lista)
print(lista_3)

liczby = [54, 999, 34, 22, 12.54, 687]
print(liczby)
liczby.sort()
print(liczby)
liczby.reverse()
print(liczby)
liczby_2 = liczby.copy()
liczby.clear()
liczby_2[0] = 6666
print(liczby_2)
print(liczby_2[0:3])
print(liczby_2[:3])
print(liczby_2[:-2])
print(liczby_2[2:])
print(liczby_2)
liczby_2.remove(54)
liczby_2.pop(0)
print(liczby_2)
print(len(liczby_2))

krotka = tuple(liczby_2)
print(krotka)
print(type(krotka))
# 13:30
