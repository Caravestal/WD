lista = [4, 6, 2, 3, 5, 9, 1]
lista2 = [7, 3, 4, 6]
suma = []

for a in lista:
    for b in lista2:
        wynik = a + b
        suma.append(wynik)
    print(suma)

# wzor do "skaładni obsługi błędów"
# try:
#     instrukcje
# except

a = input('dej liczbe a: ')
b = input('dej tez b: ')
try:
    wynik = int(a) / int(b)
    print(wynik)
except ZeroDivisionError:
    print('kurla jak to tak przez 0, kurla tak sie nie godzi')
