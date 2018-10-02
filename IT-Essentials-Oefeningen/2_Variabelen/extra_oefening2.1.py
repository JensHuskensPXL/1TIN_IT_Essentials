VAST_BEDRAG = 20
TELEFOON_BINNEN_BELGIE = 0.12
PRIJS_PER_MINUUT_BUITENLAND = 0.5
BTW = 1.21

aantal_belgische_gesprekken = int(input("Aantal belgische gespreken: "))
aantal_minuten_buitenland = int(input("Aantal minuten buitenland: "))

totaal_bedrag = (aantal_belgische_gesprekken * TELEFOON_BINNEN_BELGIE) + (aantal_minuten_buitenland * PRIJS_PER_MINUUT_BUITENLAND) * BTW + (VAST_BEDRAG / 2)
print(totaal_bedrag)