height = int(input("Wpisz swój wzrost:"))
weight = int(input("Wpisz swoją wagę:"))

bmi = (weight / (height * height) * 10000)


print(("Twoje bmi to"), round(bmi, 2))
