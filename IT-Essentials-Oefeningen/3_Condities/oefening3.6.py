basis_prijs = 5
jaar_film = int(input("Geef in hoe oud de film is in jaren: "))
rating_film = int(input("geef een rating in van 1-5: "))

if jaar_film < 2:
    prijs = basis_prijs + 1
else:
    prijs = basis_prijs
if rating_film == 1:
    prijs = prijs
elif rating_film == 2:
    prijs = prijs + 1
elif rating_film == 3:
    prijs = prijs + 1
elif rating_film == 4:
    prijs = prijs + 2
elif rating_film == 5:
    prijs = prijs + 2
if prijs > 7:
    prijs = prijs - (prijs % 7)

print("prijs bedraagd", prijs, "euro")