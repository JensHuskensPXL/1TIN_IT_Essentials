#Oefening 2.6 Schrijf code die de oppervlakte van een cirkel
# berekent, gebruik makend van variabelen straal en
# pi = 3.14159. Voor het geval je het vergeten bent,
# de formule is  straal×straal×π . Toon de uitkomst als
# volgt: “De oppervlakte van een cirkel met straal ... is ...”.

PI = 3.14159

straal = float(input("Geef de straal in m: "))

berekening_oppervlakte_cirkel = straal **2 * PI

print("De oppervlakte van de straal bedraagt", berekening_oppervlakte_cirkel, "vierkante meter.")
