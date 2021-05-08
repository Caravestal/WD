import numpy as np
from math import *

# zad.1
# Za pomocą funkcji arange stwórz tablicę numpy składającą się z 20 kolejnych wielokrotności liczby 4. 
x = np.arange(4, 20*4+4, 4)
print(x)

# zad.2
# Stwórz listę składającą się z wartości zmiennoprzecinkowych a następnie zapisz do innej zmiennej jej kopię przekonwertowaną na typ int32 
a = np.arange(2, dtype="float")
print(a)
b = a.astype("int32")
print(b)

# zad.3
# Napisz funkcję, która będzie: Przyjmowała jeden parametr ‘n’ w postaci liczby całkowitej i Zwracała tablicę Numpy o wymiarach n*n kolejnych potęg liczby 2  
def foo(n):
    temp = [2**x for x in range(1, n*n+1)]
    tab = np.array(temp)
    tab = tab.reshape((n, n))
    return tab
print(foo(4))

# zad.4
# Napisz funkcję, która będzie przyjmowała 2 parametry: liczbę, która będzie podstawą operacji potęgowania oraz ilość kolejnych potęg do wygenerowania. Korzystając z funkcji logspace generuj tablicę jednowymiarową kolejnych potęg podanej liczby, np. generuj(2,4) -> [2,4,8,16]
def foo(n, m):
    tmp = [n**x for x in range(1, m+1)]
    return tmp
print(foo(2,5))

# zad.5
# Napisz funkcję, która: 
# Na wejściu przyjmuje jeden parametr określający długość wektora; 
# Na podstawie parametru generuj wektor, ale w kolejności odwróconej; 
# Generuj macierz diagonalną z w/w wektorem na przekątnej oddalonej o 2 w górę od głównej przekątnej macierzy.
def foo(n):
    tab = np.diag([a for a in range(n, 0, -1)], 2)
    return tab
print(foo(5))

# zad.6
# Stwórz skrypt który na wyjściu wyświetli macierz numpy (tablica wielowymiarowa) w postaci wykreślanki, gdzie jedno słowo będzie wypisane w kolumnie, jedno w wierszu i jedno po ukosie. Jedno z tych słów powinno być wypisane od prawej do lewej.
tab = np.array([['B','Y','O','A','D'],['O','O','Z','L','B'],['L','A','M','A','O'],['E','S','K','B','G'],['K','D','Y','B','A']])
print(tab)

# zad.7
# Napisz funkcję, która wygeneruje macierz wielowymiarową. Przy założeniach: 
# funkcja przyjmuje parametr n, który określa wymiary macierzy jako n*n i umieszcza wielokrotność liczby 2 na kolejnych jej przekątnych rozchodzących się od głównej przekątnej. 
def foo(n):
    tab = [x*2 for x in range(1, n+1)]
    temp = []
    for x in range(0, n):
        for y in range(0, n):
            temp.append(tab[abs(x-y)])
    wyn = np.array(temp)
    wyn = wyn.reshape((n,n))
    return wyn
print(foo(10))

# zad.8
# Napisz funkcję, która: 
# jako parametr wejściowy będzie przyjmowała tablicę wielowymiarową numpy oraz parametr ‘kierunek’, 
# parametr kierunek określa czy tablica wejściowa będzie dzielona w pionie czy poziomie, 
# funkcja dzieli tablicę wejściową na pół (napisz warunek, który wyświetli komunikat, że ilość wierszy lub kolumn, w zależności od kierunku podziału, nie pozwala na operację) 
def foo(tab, kierunek):
    dlugosc = len(tab)
    szerokosc = len(tab[0])
    if kierunek == 'pionowo' and szerokosc % 2 == 0:
        tab = tab.transpose()
        tab = tab[:int(szerokosc/2)]
        return tab.transpose()
    elif kierunek == 'pionowo' and szerokosc % 2 == 1 :
        return ("Nieparzysta liczba wierszy nie pozwala na operację")
    if kierunek == 'poziomo' and dlugosc % 2 == 0:
        tab = tab[:int(dlugosc/2)]
        return tab
    elif kierunek == 'poziomo' and dlugosc % 2 == 1:
        return ("Nieparzysta liczba kolumn nie pozwala na operację")
t = np.arange(20)
t = t.reshape(4, 5)
print(foo(t, 'pionowo'))
print(foo(t, 'poziomo'))

# zad.9
# Wykorzystaj poznane na zajęciach funkcje biblioteki Numpy i stwórz macierz 5x5, która będzie zawierała kolejne wartości ciągu arytmetycznego. 
tab = np.arange(0, 50, 2)
tab = tab.reshape(5, 5)
print(tab)
