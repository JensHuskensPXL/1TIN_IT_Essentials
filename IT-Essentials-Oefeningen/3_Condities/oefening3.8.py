afstand = int(input("Geef de afstand in KM in: "))
klasse = int(input("Geef de klasse in ('1 = Toeristenklasse', '2 = cherter', '3 = zakenreis'): "))

if afstand < 1000:
    factor = 0.25
elif afstand < 2999:
    factor = 0.20
else:
    factor = 0.12

prijs = afstand * factor

if klasse == 2:
    prijs = prijs * 0.80
elif klasse == 3:
    prijs = prijs * 1.30

print("Prijs vliegtuigticket is", prijs, "euro")
