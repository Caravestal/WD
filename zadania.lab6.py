import numpy as np
# z1
# x = np.arange(4, 20*4+4, 4)
# print(x)

# z2
# a = np.arange(2, dtype="float")
# print(a)
# b = a.astype("int32")
# print(b)

# z3
# def foo(n):
#     temp = [2**x for x in range(1, n*n+1)]
#     tab = np.array(temp)
#     tab = tab.reshape((n, n))
#     return tab
# print(foo(4))

# z4
# def foo(n, m):
#     tmp = [n**x for x in range(1, m+1)]
#     return tmp
# print(foo(2,5))

# z5
# def foo(n):
#     tab = np.diag([a for a in range(n, 0, -1)], 2)
#     return tab
# print(foo(5))

# z6
# tab = np.array([['B','Y','O','A','D'],['O','O','Z','L','B'],['L','A','M','A','O'],['E','S','K','B','G'],['K','D','Y','B','A']])
# print(tab)

# z7
from math import *
# def foo(n):
#     tab = [x*2 for x in range(1, n+1)]
#     temp = []
#     for x in range(0, n):
#         for y in range(0, n):
#             temp.append(tab[abs(x-y)])
#     wyn = np.array(temp)
#     wyn = wyn.reshape((n,n))
#     return wyn
# print(foo(10))

# z8
# def foo(tab, kierunek):
#     dlugosc = len(tab)
#     szerokosc = len(tab[0])
#     if kierunek == 'pionowo' and szerokosc % 2 == 0:
#         tab = tab.transpose()
#         tab = tab[:int(szerokosc/2)]
#         return tab.transpose()
#     elif kierunek == 'pionowo' and szerokosc % 2 == 1 :
#         return ("Nieparzysta liczba wierszy nie pozwala na operację")
#     if kierunek == 'poziomo' and dlugosc % 2 == 0:
#         tab = tab[:int(dlugosc/2)]
#         return tab
#     elif kierunek == 'poziomo' and dlugosc % 2 == 1:
#         return ("Nieparzysta liczba kolumn nie pozwala na operację")
# t = np.arange(20)
# t = t.reshape(4, 5)
# print(foo(t, 'pionowo'))
# print(foo(t, 'poziomo'))

# z9
# tab = np.arange(0, 50, 2)
# tab = tab.reshape(5, 5)
# print(tab)
