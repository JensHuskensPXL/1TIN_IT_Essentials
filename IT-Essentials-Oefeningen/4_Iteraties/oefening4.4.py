gewicht_aarde = int(input("Geef je gewicht in: "))

for i in ("aarde", "maan", "jupiter", "mars"):
    if i == "aarde":
        factor = 1
    elif i == "maan":
        factor = 0.165
    elif i == "jupiter":
        factor = 2.537
    else:
        factor = 0.378
    gewicht = factor * gewicht_aarde
    print(i + ":", gewicht)