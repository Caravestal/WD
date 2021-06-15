# • załaduj dane z pliku przepis.csv jako ramkę danych,
# • ustaw jako indeksy (nazwy wierszy) kolumnę z nazwami składników,
# • stwórz wykres kołowy prezentujący procent udział składników w przepisie, podpisz każdy wycinek
# odpowiednią nazwą składnika. Wykres powinien posiadać tytuł. Każdy wycinek powinien być w innym
# kolorze. Na wykresie powinien być widoczny procentowy udział składnika w całości w zaokrągleniu do
# pełnych procentów. Początkowy kąt ustaw na 180 stopni.
# • wykres zapisz za pomocą kodu w formacie pdf.
df = pd.read_csv('przepis.csv', header=0, sep=",")
g1 = df['Waga w g'].tolist()
g2 = df['Składnik'].tolist()
plt.pie(g1, labels=g2, autopct='%1.0f%%')
starting_angle = 180
plt.title("Udzial skladnikow w przepisie")
plt.show()
plt.savefig("zad4.pdf")
