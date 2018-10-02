leeftijd = 0
aantal = 0

for i in range(1, 29):
    individueel = int(input("geef de leeftijd van de student in: "))
    leeftijd = leeftijd + individueel
    aantal =+ i

gemiddelde = leeftijd // aantal

print()
print("De gemiddelde leeftijd van de", aantal, "studenten is", gemiddelde)