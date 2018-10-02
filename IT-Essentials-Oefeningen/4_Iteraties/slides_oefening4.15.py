getal = int(input("Geef een getal in: "))

while getal % 5 != 0:
    if getal % 2 == 0:
        print("Getal", getal, "is deelbaar door 2")
    getal = int(input("Geef een getal in: "))
print("Einde")