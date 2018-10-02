naam = str(input("Geef de naam van de speler in: "))
prijs_vorig_seizoen = float(input("Geef de prijs van vorig seizoen in: "))
leeftijd = int(input("Geef de leeftijd van de speler in: "))
beoordelingscijfer = int(input("Geef het gemiddeld beoordelingscijfer in van de journalisten in ('cijfer tussen 0 en 10'): "))
type_speler = str(input("Geef type speler in ('aanvaller', 'middenvelder', 'verdediger', 'doelman'): "))
aantal_doelpunten = int(input("Geef de aantal doelpunten in ('voor keeper de doelpunten die hij niet heeft kunnen verijdelen'): "))

basis_prijs = prijs_vorig_seizoen

if leeftijd < 25:
    factor = 1.10
elif leeftijd <= 30:
    factor = 1
else:
    factor = 0.95

prijs = basis_prijs * factor

if type_speler == "aanvaller":
    if aantal_doelpunten < 5:
        factor =  10000
    else:
        facor =  20000
else:
    factor = 0

prijs = prijs + (factor * aantal_doelpunten)

if type_speler == "middenvelder" or "verdediger" or "doelman":
    factor = 10000
else:
    factor = 0

prijs = prijs + (factor * beoordelingscijfer)

if aantal_doelpunten > 20 and type_speler == "doelman":
    factor = 9000
else:
    factor = 0

prijs = prijs - (aantal_doelpunten * factor)

print("De naam van de speler:", naam)
print("Prijs van vorig seizoen was:", prijs_vorig_seizoen, "euro")
print("De nieuwe prijs bedraagd:", prijs, "euro")