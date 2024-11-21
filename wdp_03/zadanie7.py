km = int(input("Wpisz liczbe kilometrów:\n"))

if km > 30:
    print("Koszt biletu za przejazd", km, "km to", 1 + (km * 0.08), "zł.")

elif 11 <= km <= 30:
    print("Koszt biletu za przejazd", km, "km to", 10 + (km * 0.10), "zł.")

elif 0 <= km <=10:
    print("Koszt biletu za przejazd", km, "km to", 20, "zł.")
