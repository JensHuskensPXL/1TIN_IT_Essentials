getal_a = float(input("Geef getal 'a' in: "))
getal_b = float(input("Geef getal 'b' in: "))
getal_c = float(input("Geef getal 'c' in: "))

uitkomst = getal_a + getal_b

if uitkomst < 20:
    uitkomst = uitkomst + getal_c
    print("De uitkomst bedraagd:", uitkomst)
else:
    print("Te groot")