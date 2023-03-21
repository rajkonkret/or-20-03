import random

print(random.randint(1, 6))  # losuje całkowite od 1..6
print(random.random() * 10)  # 0..1 * 10 od 0..9.99999999
print(random.randrange(6))  # 0..5 całkowite
print(random.randrange(1, 6))  # 1..5 całkowite

lista = [5, 7, 6, 45, 34, 56]
print(random.choice(lista))
lista_2 = list(range(1, 50))  # list - rzutowanie na liste
print(lista_2)

wyn = random.choice(lista_2)
print(wyn)
lista_2.remove(wyn)
wyn = random.choice(lista_2)
print(wyn)
lista_2.remove(wyn)
wyn = random.choice(lista_2)
print(wyn)
lista_2.remove(wyn)
wyn = random.choice(lista_2)
print(wyn)
lista_2.remove(wyn)
wyn = random.choice(lista_2)
print(wyn)
lista_2.remove(wyn)
wyn = random.choice(lista_2)
print(wyn)
lista_2.remove(wyn)
