suma = 0
licznik = 0
while True:
    wejscie = float(input("Wprowadź liczbę\n"))
    if wejscie > 0:
        suma += wejscie
        licznik += 1
        srednia = suma / licznik
    if wejscie == 0:
        print("Suma wprowadzonych liczb to", suma, "Średnia tych liczb to:", srednia)
        break
