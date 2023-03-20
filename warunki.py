# odp = input("Czy znasz Pythona(t/n)")
#
# if odp == 't':
#     print("Brawo")
# else:
#     print("Idz sie uczyc")
#
# print("Koniec")
#
# podatek = 0.0  # float
# zarobki = int(input("Podaj dochod"))
# # powyzej 30 a ponizej 100 podatek 60%
# if zarobki < 10000:
#     podatek = 0.05
# elif zarobki < 30000:
#     podatek = 0.15
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.6
#
# print(f"Zapłacisz {zarobki * podatek} zł")

suma_zam = 124
if suma_zam > 100:
    rabacik = 25
else:
    rabacik = 0

print("rabacik", rabacik)

rabacik = 25 if suma_zam > 100 else 0
print("Rabacik 2", rabacik)

lista_bledow = []
alert_system = 'email'
alert_system = input("Podaj alert system(email,console)")
error = 'critical'
error_message = 'Stało sie coś strasznego'
if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    if error == 'medium':
        lista_bledow.append('medium')
    elif error == 'critical':
        lista_bledow.append('critical')
    else:
        lista_bledow.append('Nieznany')
# dodac warunek by bład 'critical' l dodawany do listy jako critical a nie jako nieznanyby
print(lista_bledow)
"""
wielolinijkowo
"""
