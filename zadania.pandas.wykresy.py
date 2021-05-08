import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)

# zad.1
# Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku. (imiona.xlsx)
grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
wykres = grupa.plot()
wykres.legend()
plt.title("Liczba urodzonych dzieci dla każdego roku")
plt.show()

# zad.2
# Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek z całego zbioru.
grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
wykres = grupa.plot.bar()
wykres.legend()
plt.xticks(rotation=0)
plt.title("Liczba urodzonych chłopców i dziewczynek")
plt.show()

# zad.3
# Wykres kołowy z wartościami % ukazującymi ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach z datasetu.
grupa = df[df['Rok'] > 2012].groupby(['Plec']).agg({'Liczba':['sum']})
wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20)
plt.legend()
plt.show()

# zad.4
# Wyświetl na pomocą wykresu słupkowego ilość złożonych zamówień przez poszczególnych sprzedawców (zbiór danych zamówienia.csv).
df = pd.read_csv('zamowienia.csv', delimiter=';')
policzone = df.groupby('Sprzedawca').size()
policzone.plot.bar(figsize=(6,9))
plt.ylabel("liczba zamówień")
plt.show()
