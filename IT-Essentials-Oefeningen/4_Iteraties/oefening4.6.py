artikelnummer = str(input("geef het artikelnummer in, artikelnummer eindigt altijd met 999: "))
hoeveelheid = int(input("Geef het aantal in: "))
eenheidsprijs = int(input("Geef de eenheidsprijs in: "))

totaal_bedrag = hoeveelheid * eenheidsprijs

if "999" not in artikelnummer:
    print()
    print("Fout! Het artikel nummer moet eindigen met 999!")
else:
    print()
    print("Het artikel nummer:", artikelnummer)
    print("De hoeveelheid:", hoeveelheid)
    print("De eenheidsprijs bedraagd:", eenheidsprijs, "euro")
    print("Het totale bedrag van de aankoop bedraagd:", totaal_bedrag, "euro")