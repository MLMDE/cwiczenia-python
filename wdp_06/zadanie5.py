n = int(input("Podaj liczbę n: "))

if n > 0:
   print(n)
for i in range(1, n + 1):
        potega = i * i
        print(i, "*", i, "=", potega)
