# uzycie petli while True jako głównej pętli programu
while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnozenie
    4. Dzieleniie
    5. Koniec
    """)
    wybor = input("Podaj działanie(1-2,5)")  # str
    if wybor not in ['1', '2', '3', '4']:
        break
    a = int(input("Podaj liczbe a"))  # rzutowanie na int
    b = int(input("Podaj liczbe b"))
    if wybor == '1':
        print(a + b)
    elif wybor == '2':
        print(a - b)
    elif wybor == '3':
        print(a * b)
    elif wybor == '4':
        if b != 0:
            print(a / b)
        else:
            print("Nie dzielimy przez zero")
    else:
        print("nie znam takiego działania")
