x = 5
licznik = 0
print("Odgadnij liczbę, masz na to 10 prób:")
while licznik < 10:
    wejscie = int(input("\n"))
    licznik += 1
    if licznik < 6:
        print("Pozostało", 10 - licznik, "prób.")
    if licznik > 5 and licznik < 9:
        print("Pozostały", 10 - licznik, "próby.")
    if licznik == 9:
        print("Pozostała", 10 - licznik, "próba.")
    if wejscie == 5:
        print("Zgadłeś, moja liczba to 5!")
        break
    if licznik == 10:
        print("Niestety, nie odgadłeś. Moja zdefiniowana liczba to", x)
        print()
        break
