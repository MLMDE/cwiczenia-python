maksymalna_dlugosc = int(input("Podaj maksymalną długość ciągu: "))
ciag_znakow = input("Podaj ciąg znaków: ")

dlugosc_ciagu_danych = len(ciag_znakow)

if dlugosc_ciagu_danych < maksymalna_dlugosc:
    print(f"Wprowadzony ciąg jest za krótki. Brakuje {maksymalna_dlugosc - dlugosc_ciagu_danych} znaków.")
else:
    print(f"Długość wprowadzonego ciągu jest równa lub większa od maksymalnej.")

print(f"Długość wprowadzonego ciągu: {dlugosc_ciagu_danych} znaków.")
