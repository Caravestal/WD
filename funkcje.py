# lista = []
# for element in zakres:
#     if warunem_ma_element:
#         lista.append("coś się dzieje z elementem")
# lista2 = ["Coś sie dzieje z " element for element in zakres if warunek]
#
# lista_a = []
# for x in range(10):
#     lista_a.append(x**2)
#
# a = [x**2 for x in range(10)]
# print(a)
#
# b = [3**y for y in range(6)]

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lista_parzyste = []
# for a in lista:
#     if a % 2 == 0:
#         lista_parzyste.append(a)
#
# parzyste = [a for a in lista if a % 2 == 0]

# lista = []
# for a in [1, 2, 3]:
#     for b in [4, 5, 6]:
#         lista.append([a,b])
#
# lista2 = [(i,j) for i in [1, 2, 3] for j in [4, 5, 6]]
# print(lista2)

# skroty = {"PZU": "Państwowy ubezpieczeń",
#           "ZUS": "Zakład Ubespieczeń Społecznych",
#           "PKO": "państwowa kasa oszczędnosci"}
#
# odwrocone = {}
# print(skróty)
# for key, value in skroty.items():
#     odwrocone[value] = key
#
# slownik_odwrocone = {value: key for key.value in skroty.items()}
#
# def nazwa_funkcji(arg_pozycyjne, arg_domyslne = wartosc, *arg, **arg):
#     instrukcje
#     return wartosc
# nazwa_funkcji()

# from math import *
# def rownanie_kwadratowe(a, b, c):
#     delta = b** - 4 * a * c
#     if delta < 0:
#         print("brak")
#         return 0
#     elif delta == 0:
#         print("jeden")
#         x = (-b)/(2**a)
#         return x
#     else:
#         print("2")
#         x1 = ( -b - sqrt(delta))/(2**a)
#         return x1

# def dlugosc(x1 = 0, y1 = 0, x2 = 0, y2 = 0):
#     return sqrt((x2-x1)**2 + (y2-y1)**2)
#
# print(dlugosc()) # z wartości domyślnych
# print(dlugosc(1, 2, 3, 4)) # z podanych
# print(dlugosc(x1=2, x2=4, y1=4, y2=1))
# print(dlugosc(x1=2, x2=4)) # tylko dla x podajemy, reszta dpmyślnie

# zmienna z (*liczby) robi coś w zależności czy podaliśmy listę, czy nie

from pakiet import *

a = "Ala ma kota"
litery.wyswietl(a)
print(litery.dlugosc(a))
piosenka.spiew()
