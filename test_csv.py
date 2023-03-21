# csv plik w ktorym przedzielone sa znakiem rozdzielajacym np.: ,;tab
# Radek, Kowalski, 38
# moze zawierac nagłówek z nazwami kolumn
import csv

"""
Bibliotek csw wymaga:
opcjonalnie - nazw kolumn w liscie
obowiazkowo w naszym przykłądzie danych dla wierszy w formie listy słownikow
"""

fields = ['name', 'branch', 'year', 'cgpa']
# 'Radek', 'CEO', '3', '9.1'
my_row_list = [
    {'branch': 'COE', 'cgpa': '9.1', 'name': 'Radek', 'year': '2'}
]

file = 'records.csv'

with open(file, 'w', newline='') as csv_f:  # otwieranie pliku do zapisu
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerows(my_row_list)
