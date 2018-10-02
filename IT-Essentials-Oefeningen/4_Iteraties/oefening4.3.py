aantal = 0
aantal_negatief = 0
som = 0
getal = 1

while getal != 0:
    getal = int(input("Geef een getal in: "))
    som = getal + som
    if "-" in str(getal):
        aantal_negatief += 1

print()
print("De som van de getallen is:", som)
print("Aantal negatieve getallen:", aantal_negatief)