# wzor
# for licznik in sekwencja:
#     instrukcja
# else:
#     instrukcja

for x in range(1, 6, 1):
    print(x)
else:
    print('petla zakonczona')

lista = [3, 4, 5, 1, 5]
for x in lista:
    print(x)

# wzor
# while warunek:
#     instrukcja
# else:
#     instrukcje

z = 0
while z != 10:
    print(z)
    z += 1
else:
    print('zostalo wyswietlonych ' + str(z) + ' liczb')

lista = [4, 6, 2, 3, 5, 9, 1]
liczba = input('wprowadz liczbe: ')
licznik = 0
while licznik < len(lista) - 1:
    if int(liczba) - lista[licznik] == 0
        print(liczba + ' - ' + str(lista[licznik]) + ' = 0')
        break
    else:
        licznik += 1

# wzor 
# for a in sekwencja:
#     for b in sekwencja 2:
#         instrukcje do petli 2
