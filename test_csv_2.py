import csv

filename = 'records.csv'

# w dokumentacji mamy, ze fields zapisujemy do listy, no i dostaniemy wiersze jako lisyta słownikow

fields = []
rows = []

with open(filename, 'r') as csv_f:
    csvreader = csv.reader(csv_f, delimiter=';')
    fields = next(csvreader)  # odczytaj biezacy i ustaw wskaznik na nastepny
    for row in csvreader:
        rows.append(row)
    print("Liczba wierszy", csvreader.line_num)

# print(csvreader) - przykład obiektu jaki dostajemy z biblioteki
print(fields)
print(rows)
print(rows[0][0])
