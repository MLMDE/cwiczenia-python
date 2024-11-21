pkt_egz = int(input("Wprowadź liczbę punktów zdobytych na egzaminie:\n"))

if 0 <= pkt_egz <= 50:
    print("Dwójka")
    
if 51 <= pkt_egz <= 70:
    print("Trójka")

if 71 <= pkt_egz <= 90:
    print("Czwórka")
    
if 91 <= pkt_egz <= 100:
    print("Piątka")
