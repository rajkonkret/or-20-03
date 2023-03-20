# slownik - {"name":"Radek"}
dict = {}

print(dict)
print(type(dict))
dict['imie'] = ['Radek', 'Tomek']  # dodwanie przez klucz => wartosc
dict['imie'] = 'Radek', 'Tomek'  # dodwanie przez klucz => wartosc
print(dict)
print(dict['imie'])
dict['wiek'] = 39

print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.__doc__)

dict.update({"data": "12-12-2023"})
print(dict)
dictionary = {'x': 2}
print(dictionary)
dictionary.update([('y', 3), ('z', 0)])  # dodanie dwoch par klucz=>warotsc za pomocą krotki
print(dictionary)
dictionary['x'] = 45
print(dictionary)
dictionary.pop('x')  # usuniecie po kluczu
print(dictionary)
dictionary.pop('y')
print(dictionary)

# dict_2 = {'imie': 'name', 'kot': 'cat'}
# print(dict_2['imie'])
# print("Mamy w słowniku", dict_2.keys())
# key = input("Podaj wyraz")  # zwraca str
# print(dict_2[key.lower().replace(" ", "")])

a = float(input("podaj liczbe a"))  # rzutowanie na int/float
b = float(input("podaj liczbe b"))
print(a + b)