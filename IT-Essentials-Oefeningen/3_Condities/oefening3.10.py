HUIDIG_JAAR = 2018
MINIMUM_BEDRAG = 62.5
BASIS_BEDRAG = 100

leeftijd = int(input("Geef je leeftijd in: "))
aansluitingsjaar = int(input("Geef het aansluitingsjaar in: "))

if leeftijd < 21 or leeftijd > 60:
    factor = 14.5
else:
    factor = 0

prijs = BASIS_BEDRAG - factor

prijs_per_aangesloten_jaar = (HUIDIG_JAAR - aansluitingsjaar) * 2.5

prijs = prijs - prijs_per_aangesloten_jaar

if prijs < 62.5:
    print("De prijs bedraagd 62.5 euro")
else:
    print("De prijs bedraagd:", prijs, "euro")