# definicja funkcji nie wykonuje funkcji
# funkcja kantor zwracajaca funkcje do przelicznia konkretnej waluty

kurs_eur = 4.69


def kantor(waluta):
    print("Uruchomienie kantoru")

    def usd(kwota):
        print("Przeliczam dolary, kurs 4.35")
        print(4.35 * kwota)

    def eur(kwota):
        print("Przeliczam eur, kurs", kurs_eur)
        print(kurs_eur * kwota)

    if waluta.upper() == "USD":
        return usd
    else:
        return eur


typ_waluty = input("podaj walute(eur/usd)")
moj_kantor = kantor(typ_waluty)
kwota = int(input("Podaj kwote"))
moj_kantor(kwota)
# 11:36
