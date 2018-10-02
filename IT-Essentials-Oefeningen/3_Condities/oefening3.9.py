getal1 = int(input("Geef het eerste gehele getal in: "))
getal2 = int(input("Geef het tweede gehele getal in: "))
code = int(input("Geef een bewerkingscode in ('1 = optelling', '2 = aftrekking', '3 = vermenigvuldiging', '4 = kwadraat van a', ' 5 = kwadraat van b': "))

if code <= 5:
    print("Het eerste getal is:", getal1)
    print("Het tweede getal is:", getal2)

if code == 1:
    bewerking = getal1 + getal2
    print("De bewerking bedraagd:", bewerking)
elif code == 2:
    bewerking = getal1 - getal2
    print("De bewerking bedraagd:", bewerking)
elif code == 3:
    bewerking = getal1 * getal2
    print("De bewerking bedraagd:", bewerking)
elif code == 4:
    bewerking = getal1 ** getal1
    print("De bewerking bedraagd:", bewerking)
elif code == 5:
    bewerking = getal2 ** getal2
    print("De bewerking bedraagd:", bewerking)
else:
    print("foute code")
