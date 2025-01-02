while True:
    a = int(input("Wprowadź długość boku kwadratu:\n"))
    pole = a * a
    obw = 4 * a
    if a < 0:
        print("Bok nie może być równy 0 lub być ujemny.")
        continue
    else:
        print("Pole:\n", pole, "\nObwód:\n", obw)
        continue
