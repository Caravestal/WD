lista = ['s', 3, 4.5, 1, 2, [3, 4, 5]]
print(lista)

lista.append('slowa')
lista.append(5)
print(lista)

lista.insert(3,6)
print(lista)
lista.insert(15, 5)
print(lista)

lista.pop()
print(lista)
lista.pop(1)
print(lista)

lista.remove('s')
print(lista)

del lista[5]
print(lista)

lista.reverse()
print(lista)

lista.extend((2, 2, 5))
print(lista)

lista_nowa = [5, 2, 1, 8, 3.2, 3.05, 6, 4]
lista_nowa.sort()
print(lista_nowa)
