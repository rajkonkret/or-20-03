lista = [1, 3, 14, 56, 78, 90]
# petla for po elementach
for cyfra in lista:
    if cyfra == 3:  # przyrownanie, czyli sprawdzenie czy równa sie 2
        cyfra += 1  # cyfra = cyfra + 1
    print(cyfra)

# rownowazne petle for
# for i in range(10):  # 0..9
#     if i % 2 == 0:  # reszta z dzielenia
#         print(i)
#         lista_parzyste.append(i)
list_3 = [j for j in range(10) if j % 2 == 0]  # skrotowiec
print(list_3)

imiona = ["Radek", "Zenek", "Marta"]
for p in imiona:  # petla po liscie stringow
    print(p)

# 0 Radek, 1 Zenek
# wypisanie elementow z listy str z indeksem i wartoscia
for p in range(len(imiona)):  # range(3) len = 3, czyli 0..2
    print(p + 1, imiona[p])  # imiona[p] - pobranie elementu z listy po indeksie

# uzycie enumerate zamiast iterowac po długosci listy
for p, w in enumerate(imiona):  # p -index, w = imiona[p]
    print(p + 1, w)

ludzie = ["Radek", "Janek", "Zenek", "Paulina"]
wiek = [47, 67, 32, 18]
for p, o in enumerate(ludzie):
    print(p, o)

for p, o in enumerate(ludzie):
    print(p, o, wiek[p])

# złaczenie dwoch list w jedna
for l, w in zip(ludzie, wiek):
    print(l, w)
# złaczenie i dodanie indeksu
ind = list(range(len(ludzie)))
for i, l, w in zip(ind, ludzie, wiek):
    print(i, l, w)
# 13:31
