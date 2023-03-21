# lista = []
#
# lang = input("Podaj znany Ci język programowania").lower().replace(" ", "")
#
# match lang:
#     case "python":
#         lista.append(lang)
#     case "java":
#         lista.append(lang)
#     case "c++":
#         lista.append(lang)
#     case _:  # wartosc domyslna
#         print("nie znam takiego języka")
#
# print(lista)

# Prosicie uzytkownika o date Chrztu Polski i weryfikujecie czy podał prawidłowo
odp = int(input("Podaj date Chrztu Polski"))  # input zawsze zwraca string, int rzutuje na integer

match odp:
    case 966:
        print("Ok")
    case _:
        print("Ksiazka od historii na drugiej półce")
# 10:11
