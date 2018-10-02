sterren = int(input("Geef het aantal sterren in (1-5): "))
code = str(input("Geef het verzorgingstype in ('O = enkel ontbijt', 'H = halfpension', 'V = vol pension', 'A = all-inclusive': "))
aantal_overnachtingen = int(input("Geef het aantal overnachtingen in: "))
seizoen = str(input("Geef het seizoen in ('H =  hoogseizoen', 'L = laagseizoen', 'T = tussenseizoenen': "))

if sterren == 1:
    nacht = 30
elif sterren == 2 or sterren == 3:
    nacht = 40
else:
    nacht = 55

prijs = nacht * aantal_overnachtingen

if code == "o" or code == "O":
    prijs = prijs * 1.20
elif code == "h" or code == "H":
    prijs = prijs * 1.50
elif code == "v" or code == "V":
    prijs = prijs * 1.60
else:
    prijs = prijs * 1.60 + 80

if code == "o" or code == "O":
    if seizoen == "L" or seizoen == "l":
        prijs = prijs * 0.90

if code == "h" or code == "H":
    if seizoen == "L" or seizoen == "l":
        prijs = prijs * 0.90

print("De prijs voor de vakantie van 1 persoon bedraagd:", prijs)