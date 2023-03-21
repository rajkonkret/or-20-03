import random

# for - iteruje po indeksie

lista_parzyste = []
for i in range(10):  # 0..9
    if i % 2 == 0:  # reszta z dzielenia
        print(i)
        lista_parzyste.append(i)

print(lista_parzyste)

lista_wyn = []
lista_lotto = list(range(1, 50))  # 1..49
for i in range(6):  # 0..5
    wyn = random.choice(lista_lotto)
    # print(wyn)
    lista_lotto.remove(wyn)
    lista_wyn.append(wyn)

lista_wyn.sort()

# print(sorted(lista_wyn))
print(lista_wyn)
with open('liczby.txt', 'w', encoding='utf-8') as f:  # f = filehandler
    f.write(str(lista_wyn))
