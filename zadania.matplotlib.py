import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)

# zad.1,2
y = [1/y for y in range(1, 21)]
x = [x for x in range(1, 21)]
plt.plot(x, y, 'g^--', label='f(x)=1/x')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Wykres funkcji f(x) dla x[1,20]")
plt.show()

# zad.3
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
# nie wykrywa strony

# zad.6
grupa = df[df['Plec'] == 'K'].agg({'Liczba': ['sum']})
grupa = grupa['Liczba'].values[0]
grupa2 = df[df['Plec'] == 'M'].agg({'Liczba': ['sum']})
grupa2 = grupa2['Liczba'].values[0]
plt.subplot(1, 3, 1)
dane = [grupa, grupa2]
etykiety = ['Kobiety', 'Mężczyźni']
plt.title("K i M")
wykres = plt.bar(etykiety, dane)

gr = df[df['Plec'] == 'K'].groupby(['Rok']).agg({'Liczba': ['sum']})
gr2 = df[df['Plec'] == 'M'].groupby(['Rok']).agg({'Liczba': ['sum']})
plt.subplot(1, 3, 2)
plt.xlabel('Rok')
plt.ylabel('Ilosc')
plt.title("K i M (rok)")
plt.plot(gr)
plt.plot(gr2)

g = df.groupby(['Rok']).agg({'Liczba': ['sum']})
plt.subplot(1, 3, 3)
plt.xlabel('Rok')
plt.ylabel('Ilosc')
g.plot.bar()
plt.show()

# zad.7
dz = pd.read_csv('zamowienia.csv', delimiter=';')
grupa = dz.groupby(['Sprzedawca']).size()
wykres = grupa.plot.pie(subplots=True, autopct='%.f %%', fontsize=20, explode=[0, 0.1, 0, 0, 0.2, 0, 0, 0, 0], shadow=True)
plt.show()
