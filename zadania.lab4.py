# zad.1
# import random
# lista1 = []
# i = 1
# plik = open("C:/Users/Marta/OneDrive - University of Warmia and Mazuria in Olsztyn/Dokumenty/C++WDP/WD.txt", "w+")
# while i <= 10:
#     plik.write(str(2*(random.randint(0,30))) + "\n")
#     i = i + 1
#
# plik.close()

# zad.2
# with open("C:/Users/Marta/OneDrive - University of Warmia and Mazuria in Olsztyn/Dokumenty/C++WDP/WD.txt", 'r') as plik:
#     for x in plik:
#         print(x)

# zad.3
# with open("C:/Users/Marta/OneDrive - University of Warmia and Mazuria in Olsztyn/Dokumenty/C++WDP/WD.txt", 'w') as plik:
#     plik.write("jakies zdanie\n")
#     plik.write("jakies zdanie 2")
# with open("C:/Users/Marta/OneDrive - University of Warmia and Mazuria in Olsztyn/Dokumenty/C++WDP/WD.txt", 'r') as plik:
#     for x in plik:
#         print(x)

# zad.4
# class NaZakupy:
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#     def wyswietl_produkt(self):
#         print(self.nazwa_produktu + '\n' + str(self.ilosc) + '\n' + self.jednostka_miary + '\n' + str(self.cena_jed))
#     def ile_produktu(self):
#         print(str(self.ilosc) + self.jednostka_miary)
#     def ile_kosztuje(self):
#         print(str(self.cena_jed * self.ilosc))
#
# zakupki = NaZakupy('chlieb', 1, 'bohen', 3)
# zakupki.wyswietl_produkt()

# zad.5
# class CiagAr:
#     lista = []
#     def __init__(self, wartosc_p, roznica, ilosc):
#         self.wartosc_p = wartosc_p
#         self.roznica = roznica
#         self.ilosc = ilosc
#     def wyswietl_dane(self):
#         print(self.lista)
#     def pobierz_elementy(self):
#         for x in range(6):
#             self.lista.append(int(input()))
#     def pobierz_parametry(self):
#         or x in range(self.wartosc_p, self.roznica, self.ilosc):
#         self.lista.append(x)
#     def policz_sume(self):
#         print(sum(self.lista))
#     def policz_elementy(self):
#         if self.roznica != 0:
#             self.wynik = 0
#             for x in self.lista:
#                 self.wynik = self.wynik + 1
#             return self.wynik
#         else:
#             return 0

# zad.6
# class Robaczek:
#     def __init__(self, x, y, krok):
#         self.x = x
#         self.y = y
#         self.krok = krok
#     def idz_w_gore(self, ile_krokow):
#         self.y = self.y + (self.krok * ile_krokow)
#     def idz_w_dol(self, ile_krokow):
#         self.y = self.y + ((-1)*(self.krok * ile_krokow))
#     def idz_w_lewo(self, ile_krokow):
#         self.x = self.x + ((-1)*(self.krok * ile_krokow))
#     def idz_w_prawo(self, ile_krokow):
#         self.x = self.x + (self.krok * ile_krokow)
#     def pokaz_gdzie_jestes(self):
#         print('x: ' + str(self.x) + 'y: ' + str(self.y))
