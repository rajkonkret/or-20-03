# funkcja liczy sumę
# dodaj obliczanie średniej

def liczby(c, *cyfry):
    print(c)
    print(cyfry)
    print(type(cyfry))
    suma = 0
    for i in cyfry:
        suma += i  # suma = suma + i
    print(f"Suma {suma}")
    count = len(cyfry)
    if count != 0:
        sred = suma / count
        print(f"Srednia {sred}")


liczby(1)
liczby(1, 2)
liczby(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
