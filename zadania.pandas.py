import pandas as pd
import numpy as np
import xlrd
import openpyxl

# zad.1
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)

# zad.2
# tylko te rekordy gdzie liczba nadanych imion była mniejsza niż 1000 w danym roku
# print(df[df['Liczba'] < 1000])

# tylko rekordy gdzie nadane imię jest takie jak Twoje
# print(df[df['Imie'] == 'MARTA'])

# sumę wszystkich urodzonych dzieci w całym danym okresie
# print(df.agg({'Liczba': ['sum']}))

# sumę dzieci urodzonych w latach 2005-2010
# print(df[(df['Rok'] < 2010) & (df['Rok'] > 2005)].agg({'Liczba': ['sum']}))

# sumę urodzonych chłopców w 2000 roku
# print(df[(df['Rok'] == 2000) & (df['Plec'] == 'M')].agg({'Liczba': ['sum']}))

# najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok)
# print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth(0))

# najbardziej popularne imię dziewczynki i chłopca w całym danym okresie
# new_df = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
# for index, group in enumerate(new_df, start=1):
#     print(f"{index} {group[0]}")
#     print(f" {group[1].iloc[0]['Imie']}", end='')
#     print(f" {group[1].iloc[0]['Liczba']}")
#
# print("Chłopiec")
# print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba':['sum']}).sort_values(('Liczba','sum'), ascending=False).iloc[0])
# print("Dziewczynka")
# print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'), ascending=False).iloc[0])

# zad.3
df = pd.read_csv('zamowienia.csv', header=0, sep=";", decimal=',')
# print(df)

# lista unikalnych nazwisk sprzedawców
# print(df['Sprzedawca'].unique())

# 5 najwyższych wartości zamówień
# print(df.sort_values(by='Utarg', ascending=False)['Utarg'][0:5])

# ilość zamówień złożonych przez każdego sprzedawcę
# print(df.groupby(['Sprzedawca']).size())

# suma zamówień dla każdego kraju
# print(df.groupby(['Kraj']).agg({'Utarg':['sum']}))

# suma zamówień dla roku 2005, dla sprzedawców z Polski
# print(df[((df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31') & (df['Kraj'] == 'Polska'))].agg({'Utarg':['sum']}))

# średnią kwotę zamówienia w 2004 roku,
# print(df[((df['Data zamowienia'].str[:4] == '2004'))]['Utarg'].mean())

# zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv
# rok_2004 = df[((df['Data zamowienia'].str[:4] == '2004'))]
# rok_2005 = df[((df[ 'Data zamowienia'].str[:4] == '2005'))]
# rok_2004.to_csv("zamowienia_2004.csv", sep=';', index=False)
# rok_2005.to_csv("zamowienia_2005.csv", sep=';', index=False)
