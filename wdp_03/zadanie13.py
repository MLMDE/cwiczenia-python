doby = int(input("Podaj liczbę dób pobytu: "))

if doby > 7:
    oplata = 50 * doby
elif 4 <= doby <= 7:
    oplata = 75 * doby
else:
    oplata = 100 * doby

print("Całkowita opłata za pobyt wynosi:", oplata, "zł")
