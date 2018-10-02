#Oefening 2.8 Wat kost mijn auto? Prijsbewuste personen willen
# weten hoeveel hun auto echt kost. Achtereenvolgens wordt
# ingevoerd:

# aantal afgelegde km per jaar (afgelegde_km)
# verbruik in l per 100 km (verbruik)
# prijs van 1 l brandstof (prijs_per_liter)
# Als uitvoer wordt verwacht:
#
# de totale kosten per jaar voor het opgegeven aantal km
# de kostprijs per km rijden.

afgelegde_km = float(input("Aantal afgelegde KM per jaar : "))
verbruik = float(input("Verbruik in L per 100km: "))
prijs_per_liter = float(input("Prijs van 1 L brandstof: "))

totale_kosten_per_jaar = prijs_per_liter * verbruik * afgelegde_km / 100
kostprijs_per_km = totale_kosten_per_jaar / afgelegde_km

print("Totale kosten per jaar: €", totale_kosten_per_jaar)
print("Kostprijs per km: €", kostprijs_per_km)


# voorbeeld
# 1.35 prijs per l
# 7 L per 100 km
# 17000 km afgelegd