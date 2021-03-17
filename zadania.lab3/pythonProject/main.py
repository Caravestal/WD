# zad.1
# a = [1-x for x in range(1, 10)]
# b = [4**x for x in range(0, 7)]
# c = [x for x in b if(x % 2 == 0)]
# print(a, b, c)
#
# zad.2
# import random
# lista1 = []
# i = 1
# while i <= 10:
#     lista1.append(random.randint(0,9))
#     i = i + 1
# print(lista1)
# lista2 = [x for x in lista1 if(x % 2 == 0)]
# print(lista2)
#
# zad.3
# slownik = {'chleb': '1 szt', 'maslo': '1 kg', 'ziemniaki': '1 kg', 'bulka': '1 szt'}
# lista = [key for key, value in slownik.items() if value == '1 szt']
# print(lista)
#
# zad.4
# def trojkatpro(a, b, c):
#     if a**2 + b**2 == c**2:
#         print('tojkat prostokatny')
#     else:
#         print('trojkat nie jest prostokatny')
#
# zad.5
# def trapez(a=19, b=11, h=7):
#     pole = ((a + b) * h) / 2
#     return pole
# print(trapez())
#
# zad.6
# def foo( a=1, b=4, ile = 10):
#     i = 1
#     while i<=10:
#         a *= b
#         print(a)
#         i += 1
# print(foo())
#
# zad.7
# def foo( a=1, b=4, ile = 10):
#     i = 1
#     while i<=10:
#         a *= b
#         print(a)
#         i += 1
# print(foo())
#
# zad.8
# def foo(a):
#     wynik = 0
#     x = 0
#     for values in a.values():
#         wynik += values
#         x += 1
#     return wynik,x
#
# zakupy = {'chleb': 2, 'maslo': 4, 'berlinki': 9, 'bulki': 12}
# print(foo(zakupy))
#
# zad.9
# from ciagi import *

