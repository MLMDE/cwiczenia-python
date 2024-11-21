liczba_egz = int(input("Wprowadź liczbę egzemplarzy:\n"))

if liczba_egz > 1000:
    print("Cena druku egzemplarzy wynosi", liczba_egz * 10, "zł.")
elif liczba_egz < 500:
    print("Cena druku egzemplarzy wynosi", liczba_egz * 15, "zł.")
elif 500 <= liczba_egz <= 1000:
    print("Cena druku egzemplarzy wynosi", liczba_egz * 12, "zł.")
