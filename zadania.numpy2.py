import numpy as np
from math import *
# zad.1
# a = np.arange(3, 9, 2)
# print(a)
# b = np.array([4, 6, 7])
# print(b)
# print(a * b)
#
# zad.2
# a = np.arange(16).reshape(4, 4)
# b = np.arange(9).reshape(3, 3)
# print(b)
# print("")
# print(a)
# w = 0
# w2 = 0
# for x in b:
#     min = x[0]
#     for y in range(1, len(x)):
#         if x[y] <= min:
#             min = x[y]
#     print("w b dla wiersza " + str(w) + " najmiejasza jest " + str(min))
#     w = w + 1
#
# for x in a:
#     min = x[0]
#     for y in range(1, len(x)):
#         if x[y] <= min:
#             min = x[y]
#     print("w a dla wiersza " + str(w2) + " najmiejasza jest " + str(min))
#     w2 = w2 + 1
#
# tempb = b.T
# tempa = a.T
# print(tempb)
# print(tempa)
# w3 = 0
# w4 = 0
# for x in tempb:
#     min = x[0]
#     for y in range(1, len(x)):
#         if x[y] <= min:
#             min = x[y]
#     print("w b dla kolumny " + str(w3) + " najmiejasza jest " + str(min))
#     w3 = w3 + 1
#
# for x in tempa:
#     min = x[0]
#     for y in range(1, len(x)):
#         if x[y] <= min:
#             min = x[y]
#     print("w a dla kolumny " + str(w4) + " najmiejasza jest " + str(min))
#     w4 = w4 + 1

# zad.3
# a = np.arange(3, 9, 2)
# print(a)
# b = np.array([4, 6, 7])
# print(b)
# print(a.dot(b))

# zad.4
# a = np.array([4, 6, 7])
# b = np.array([1, 9, 8])
# print(a * b)

# zad.5
# aa = []
# n = np.arange(6).reshape(2, 3)
# print(n)
# for x in n:
#     for y in x:
#         aa.append(sin(y))
# a = np.array([aa])
# print(a)
#
# # zad.6
# bb = []
# m = np.array([[4, 6, 7], [1, 4, 7]])
# print(m)
# for x in m:
#     for y in x:
#         bb.append(cos(y))
# b = np.array([bb])
# print(b)
#
# # zad.7
# print(a + b)

# zad.8
# b = np.arange(9).reshape(3, 3)
# for x in b:
#     print(x)

# zad.9
# b = np.arange(9).reshape(3, 3)
# for x in b.flat:
#     print(x)
#     print("")

# zad.10
# a = np.arange(81).reshape(9, 9)
# print(a)
# a = a.reshape(3, 27)
# print(a)
# a = a.T
# print(a)
# a = a.ravel()
# print(a)

# zad.11
# a = np.arange(12).reshape(3, 4)
# print(a)
# for x in a.flat:
#     print(x)
#     print("")
# b = np.arange(12).reshape(4, 3)
# print(b)
# for x in b.flat:
#     print(x)
#     print("")
# c = np.arange(12).reshape(2, 6)
# print(c)
# for x in c.flat:
#     print(x)
#     print("")
