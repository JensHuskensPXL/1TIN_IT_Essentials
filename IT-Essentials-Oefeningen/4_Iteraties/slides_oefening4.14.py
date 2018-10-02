leeftijd = 0
aantal = 0

while aantal < 28:
    individueel = int(input("Geef de leeftijd van student " + str(aantal + 1) + " in: "))
    leeftijd = leeftijd + individueel
    aantal = aantal + 1 #HET WAAR OF HET ONWAAR MAKEN VAN DE CONDITIE MOET MEESTAL GEBEUREN ALS LAATSTE ZIN VAN DE WHILE BLOCK

gemiddelde = leeftijd // aantal

print()
print("De gemiddelde leeftijd van de", aantal, "studenten is", gemiddelde)