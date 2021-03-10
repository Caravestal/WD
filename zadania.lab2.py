# zad.1
# lista = ['film1', 'film2', 'film3', 'film4', 'film5']
# lista.reverse()
# print(lista)
# lista.insert(5, 'film6')
# lista.insert(6, 'film7')
# lista.insert(7, 'film8')
# lista.insert(8, 'film9')
# lista.insert(9, 'film10')
# print(lista)
#
# zad.2
# slownik = {1: 'film1', 2: 'film2', 3: 'film3', 4: 'film4', 5:'film5'}
#
# zad.3
# slownik = {'md': 'matematyka dyskretna', 'ps': 'programowanie strukturalne', 'wd': 'wizualzacja danych', 'am': 'analiza matematyczna'}
# print(str(len(slownik)))
#
# zad.4
# a = int(input('daj liczbe: '))
# a = a**a
# print(a)
#
# zad.5
# import sys as system
# litery = system.stdin.readline()
# system.stdout.write(str(litery.count("a")))

# zad.6
# a = int(input('dej liczbe a: '))
# b = int(input('dej liczbe b: '))
# c = int(input('dej liczbe c: '))
# if (a % 2 = 0) & (b > c):
#     print('warunek jest spelniony')
# else:
#     print('nie')
#
# zad.7
# lista = [1, 2, 4.5, 3.6]
# for x in range(1, len(lista)):
#     print(lista[x-1] + lista[x])

# zad.8
# lista = []
# i=0
# while i<=9:
#     x = int(input())
#     if x % 2 == 0:
#         lista.append(x)
#     i=i+1
# print(lista)

# zad.9
# import sys as system
# lista = [1, 2, 3, 4, 5, 6]
# for a in lista:
#     if (a == 1) | (a == 6):
#         for v in lista:
#             system.stdout.write("O")
#         system.stdout.write("\n")
#     else:
#         system.stdout.write("O")
#         for b in range(4):
#             system.stdout.write(" ")
#         system.stdout.write("O")
#         system.stdout.write("\n")
#
# zad.10
# try:
#     a = float(input("dej cyfre: "))
# except ValueError:
#     print("skandal")
