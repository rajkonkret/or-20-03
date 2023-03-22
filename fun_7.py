# To tylko definicja funkcji
# w tym miejscu funkcja sie nie wykonuje
# system tylko zapamietuje gdzie jest funkcja
def connect(**opcje):
    print(opcje)
    connect_param = {
        'host': '127.0.0.7',
        'port': '8080'
    }
    # dodanie do słownika connect_param klucza pwd i nadanie wartosci ze zmiennej lokalnej opcje
    connect_param['pwd'] = opcje
    print(connect_param)


# ** oczekiwane argumenty w postaci klucz, wartosc np.: user='/home'
connect(user='/home')
connect(root='/')
connect(root='/', opt='/opt')
# {'root': '/', 'opt': '/opt'} - to przyszło w opcjach
# {'host': '127.0.0.7', 'port': '8080', 'pwd': {'root': '/', 'opt': '/opt'}} - tak po dodaniu do wewnetrznego słownika
