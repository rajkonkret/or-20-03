import requests as re

# pip install request
url = "http://api.nbp.pl/api/exchangerates/rates/A/USD/"
response = re.get(url)
print(response)
# 200 ok
# 4 ..bledy
# 5 bledy serwera
table = response.json()
print(table)
print(table['rates'])
print(table['rates'][0])
print(table['rates'][0]['mid'])

# NumPy
# Pandas - excel
# matplotlib - wykresy
# Qt, Tkinter
# sqlite
