# set - nie przechowuje zdublowanych elementow
lista = [44, 55, 66, 77, 33, 22, 11, 33, 11]
# {33, 66, 11, 44, 77, 22, 55}
zbior = set(lista)
print(zbior)
zbior.add(33)
print(zbior)
zbior.add(18)
print(zbior)
print(zbior.pop())
print(zbior.pop())

zbior_2 = {66, 11, 44, 18, 55, 62, 999}
print(zbior_2)
print(sorted(zbior_2))  # zwraca posortowana liste
print(zbior | zbior_2)  # suma zbiorow
print(zbior & zbior_2)  # czesc wspolna
print(zbior - zbior_2)
print(zbior.difference(zbior_2))
print(zbior_2.difference(zbior))
empty = set()  # pusty set
