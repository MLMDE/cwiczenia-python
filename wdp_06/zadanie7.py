liczba = int(input("Wprowadź liczbę:\n"))
suma = 0  

liczba_str = str(liczba)    

for cyfra in liczba_str: 
    suma += int(cyfra)  
print("Suma cyfr liczby", liczba, "wynosi:\n", suma)
