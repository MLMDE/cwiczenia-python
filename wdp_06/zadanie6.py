n = int(input("Wprowadź liczbę n:\n"))

x = input("ile liczb ma być wyświetlonych po Twojej liczbie?\n")

z = int(x)

for i in range(0, n + z):
    if i % 3 == 0:
        print(i, end=" ")
