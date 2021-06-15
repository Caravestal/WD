# Wykres kołowy
df = pd.read_csv('przepis.csv', header=0, sep=",")
g1 = df['Waga w g'].tolist()
g2 = df['Składnik'].tolist()
plt.pie(g1, labels=g2, autopct='%1.0f%%')
starting_angle = 180 #początkowy kąt
plt.title("Udzial skladnikow w przepisie")
plt.show()
plt.savefig("zad4.pdf") #zapis pdf

# Wykres z sąsiadującymi słupkami
nazwa = np.arange(5)
print(nazwa)
wartosci1 = [10, 85, 82, 38, 50]
wartosci2 = [60, 42, 72, 93, 75]
wartosci3 = [83, 95, 67, 30, 42]
plt.bar(nazwa, wartosci1, width=0.25, label='B', color='#6DCCA1')
plt.bar(nazwa+0.25, wartosci2, width=0.25, label='C', color='#D39F6C')
plt.bar(nazwa+0.5, wartosci3, width=0.25, label='A', color='#0F99AC')
plt.xticks([0.25, 1.25, 2.25, 3.25, 4.25], [0, 1, 2, 3, 4]) #służy do pobierania lub ustawiania bieżących lokalizacji i etykiet osi x.
plt.grid(axis='y')
plt.title('Wykres')
plt.legend()
plt.show()
