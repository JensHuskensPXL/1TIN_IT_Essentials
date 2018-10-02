VAST_RECHT = 25

verbruikt_water = int(input("Geef het aantal verbruikte water in (in vierkante meter): "))

if verbruikt_water <= 30:
    factor = 0
elif verbruikt_water <= 200:
    factor = 1
elif verbruikt_water <= 5000:
    factor = 1.25
else:
    factor = 1.175

prijs = VAST_RECHT + (factor * verbruikt_water)

print("Het te betalen bedrag bedraagd:", prijs, "euro")