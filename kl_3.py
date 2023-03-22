class Dom:
    """
    Klasa opisująca dom w pythonie
    """

    def __init__(self, metraz):
        self.__metraz = metraz  # pole prywatne, brak mozliwosci zmiany bez uzycia funkcji typu seter

    def zmien_metraz(self):
        wybor = input("Podaj metraz")
        self.__metraz = int(wybor)
        print("Teraz masz metraz:", self.__metraz)
        self.__farba()

    def __farba(self):      # funkcja prywatna, mozliwe wywołanie z wnetrza klasy tylko
        print("Brakło farby")


dom_1 = Dom(190)
# te 3 linijki nie zadziałąja, bo ustawilismy pole prywatne __metraz
# print(dom_1.metraz)
# dom_1.metraz = 340
# print(dom_1.metraz)
dom_1.zmien_metraz()
