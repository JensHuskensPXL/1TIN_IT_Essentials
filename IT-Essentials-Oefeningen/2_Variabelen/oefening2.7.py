#Oefening 2.7 Schrijf een programma dat de kosten berekent
# voor het plaatsen van kamerbreed tapijt. De gebruiker van
#het programma geeft de lengte en breedte van het tapijt in
# (uitgedrukt in meter), de prijs per m2 en de plaatsingskosten
#  per m2 in. Als resultaat moet de kostprijs van het tapijt,
# de plaatsingskosten en de totale kosten afgedrukt worden.

lengte_tapijt = float(input("Lengte tapijt in meter: "))
breedte_tapijt = float(input("Breedte tapijt in meter: "))
prijs_per_m2 = float(input("Prijs per m2: "))
prijs_plaatsingskosten_per_m2 = float(input("Prijs plaatsingskosten per m2: "))

kostprijs_tapijt = lengte_tapijt * breedte_tapijt * prijs_per_m2
plaatsingskosten = lengte_tapijt * breedte_tapijt * prijs_plaatsingskosten_per_m2
totale_kosten = kostprijs_tapijt + plaatsingskosten

print("kostprijs tapijt : €", kostprijs_tapijt)
print("plaatsingskosten : €", plaatsingskosten)
print("Totale kosten: €", totale_kosten)
