import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)

# zad.1,2
# Na wykresie wyświetl wykres liniowy funkcji f(x) = 1/x dla x ϵ [1, 20]. Dodaj etykietę do linii wykresu i wyświetl legendę. 
# Dodaj odpowiednie etykiety do osi wykresu (‘x’, ’f(x)’) oraz ustaw zakres osi na (0, 1) oraz (1, długość wektora x). 
# Zmodyfikuj wykres z zadania 1 tak, żeby styl wykresu wyglądał tak jak na poniższym zrzucie ekranu. 
y = [1/y for y in range(1, 21)]
x = [x for x in range(1, 21)]
plt.plot(x, y, 'g^--', label='f(x)=1/x')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Wykres funkcji f(x) dla x[1,20]")
plt.show()

# zad.3
# Na jednym wykresie wygeneruj wykresy funkcji sin(x) oraz cos(x) dla x ϵ [0, 30] z krokiem 0.1. Dodaj etykiety i legendę do wykresu. 
from math import *
a = np.arange(0, 30, 0.1)
b = np.sin(a)
c = np.cos(a)
plt.plot(a, b, 'g', label='sin(x)')
plt.plot(a, c, 'r', label='cos(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('sin(x) i cos(x)')
plt.title("Wykres funkcji sin(x) i cos(x) dla x[0,30]")
plt.show()

# zad.4
# Dodaj drugi wykres funkcji sinus do zadania 3 i zmodyfikuj parametry funkcji, tak aby osiągnąć efekt podobny do tego na poniższym zrzucie ekranu. 
x = np.arange(0, 30, 0.1)
b = np.sin(x)
c = np.sin(x*(-1))-2
plt.plot(x, b, '#339999', label='sin(x)')
plt.plot(x, c, '#FFCC33', label='sin(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title("Wykres sin(x), sin(x)")
plt.show()

# zad.5
# Korzystając ze zbioru danych Iris (https://archive.ics.uci.edu/ml/datasets/iris) wygeneruj wykres punktowy, 
# gdzie wektor x to wartość ‘sepal length’ a y to ‘sepal width’, 
# dodaj paletę kolorów c na przykładzie listingu 6 a parametr s niech będzie wartością absolutną z różnicy wartości poszczególnych elementów wektorów x oraz y. 
df = pd.read_csv('iris.data', sep=',', decimal='.', header=None)
print(df)
# przygotowanie wektora kolorów
colors = np.random.randint(0, 50, len(df.index))
# przygotowanie wektora z rozmiarami 'kropek'
# scale = [np.abs(df[0].iloc[x] - df[1].iloc[x]) for x in range(len(df.index))]
# można te wielkości troszeczkę 'podrasować'
scale = [np.abs(df[0].iloc[x] - df[1].iloc[x]) * 5 for x in range(len(df.index))]

plt.scatter(df[0], df[1], c=colors, s=scale)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()

# zad.6
# Korzystając z biblioteki pandas wczytaj zbiór danych z narodzinami dzieci przedstawiony w lekcji 8. 
# Następnie na jednym płótnie wyświetl 3 wykresy (jeden wiersz i 3 kolumny). 
# Dodaj do wykresów stosowne etykiety. Poustawiaj różne kolory dla wykresów. 
# 1 wykres – wykres słupkowy przedstawiający ilość narodzonych dziewczynek i chłopców w całym okresie. 
plt.subplot(1, 3, 1)
grouped = df.groupby('Plec').agg({'Liczba': ['sum']}).unstack()
grouped.plot.bar(color=['r', 'g'])
plt.xlabel('Płeć')

# 2 wykres – wykres liniowy, gdzie będą dwie linie, jedna dla ilości urodzonych kobiet, druga dla mężczyzn dla każdego roku z osobna. 
# Czyli y to ilość narodzonych kobiet lub mężczyzn (dwie linie), x to rok. 
plt.subplot(1, 3, 2)
x = df['Rok'].unique()
kobiety = df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba':['sum']}).values
mezczyzni = df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba':['sum']}).values
plt.plot(x, kobiety, label="Kobiety")
plt.plot(x, mezczyzni, label="Mężczyźni")
plt.ylabel('Liczba narodzonych dzieci')

# 3 wykres – wykres słupkowy przedstawiający sumę urodzonych dzieci w każdym roku. 
plt.subplot(1, 3, 3)
x = df['Rok'].unique()
# bez funkcji flatten matplotlib wyrzuca wyjątek, który informuje nas, że nie można
# przekazywać parametru jako tablicy wielowymiarowej a w takiej postaci w tym przypadku
# zwracany jest wektor y, korzystamy więc z flatten() poznanej przy okazji omawiania biblioteki numpy
y = df.groupby('Rok').agg({'Liczba':['sum']}).values.flatten()

plt.bar(x, y)

# wyświetlamy cały wykres
plt.show()

# zad.7
# Korzystając z pliku zamówienia.csv (Pandas) 
# policz sumy zamówień dla każdego przedawcy i wyświetl wykres kołowy z procentowym udziałem każdego sprzedawcy w ogólnej sumie zamówień. 
# Poszukaj w Internecie jak dodać cień do takiego wykresu i jak działa atrybut ‘explode’ tego wykresu. 
# Przetestuj ten atrybut na wykresie. 
dz = pd.read_csv('zamowienia.csv', delimiter=';')
grupa = dz.groupby(['Sprzedawca']).size()
wykres = grupa.plot.pie(subplots=True, autopct='%.f %%', fontsize=20, explode=[0, 0.1, 0, 0, 0.2, 0, 0, 0, 0], shadow=True)
plt.show()
