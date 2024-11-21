print("0 - niedziela")
print("1 - poniedziałek")
print("2 - wtorek")
print("3 - środa")
print("4 - czwartek")
print("5 - piątek")
print("6 - sobota")

pytanie = int(input("\nWybierz dzień tygodnia z listy\n"))

pn = "Urząd jest czynny od 10 do 14."
wt = "Urząd jest czynny od 10 do 19."
sr_pt = "Urząd jest czynny od 11 do 16."
so_nd = "Urząd jest nieczynny."

if pytanie == 0:
    print(so_nd)
elif pytanie == 1:
    print(pn)
elif pytanie == 2:
    print(wt)
elif pytanie == 3:
    print(sr_pt)
elif pytanie == 4:
    print(sr_pt)
elif pytanie == 5:
    print(sr_pt)
elif pytanie == 6:
    print(so_nd)
