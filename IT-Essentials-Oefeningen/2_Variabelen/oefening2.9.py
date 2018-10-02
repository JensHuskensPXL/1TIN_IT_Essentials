#Oefening 2.9 Schrijf code die een hoeveelheid centen
# (opgeslagen in een variabele met de naam bedrag)
# classificeert als een combinatie van grotere geldstukken.
# Je code gebruikt 2 euro's (200 centen), euro's (100 centen),
#  50 centen, 20 centen, 10 centen, 5 centen, 2 centen en centen
# (1 cent). Het resultaat is dat je het bedrag uitdrukt in het
# minimale aantal muntjes dat nodig is.

#Voorbeeld: 359 centen = 1  ×  2 euro, 1  ×  1 euro,
# 1  ×  50 cent, 0  ×  20 cent, 0  ×  10 cent, 1  ×  5 cent,
# 2  ×  2 cent en 0  ×  1 cent.


bedrag = int(input("Hoeveelheid centen: "))

euro_2 = int(bedrag / 200)
euro_1 = int((bedrag - euro_2 * 200) / 100)
cent_50 = int((bedrag - euro_2 * 200 - euro_1 * 100) / 50)
cent_20 = int((bedrag - euro_2 * 200 - euro_1 * 100 - cent_50 * 50) / 20)
cent_10 = int((bedrag - euro_2 * 200 - euro_1 * 100 - cent_50 * 50 - cent_20 * 20) / 10)
cent_5 = int((bedrag - euro_2 * 200 - euro_1 * 100 - cent_50 * 50 - cent_20 * 20 - cent_10 * 10) / 5)
cent_2 = int((bedrag - euro_2 * 200 - euro_1 * 100 - cent_50 * 50 - cent_20 * 20 - cent_10 * 10 - cent_5 * 5) / 2)
cent_1 = int((bedrag - euro_2 * 200 - euro_1 * 100 - cent_50 * 50 - cent_20 * 20 - cent_10 * 10 - cent_5 * 5 - cent_2 * 2) / 1)

print(euro_2, "x 2 euro")
print(euro_1, "x 1 euro")
print(cent_50, "x 50 cent")
print(cent_20, "x 20 cent")
print(cent_10, "x 10 cent")
print(cent_5, "x 5 cent")
print(cent_2, "x 2 cent")
print(cent_1, "x 1 cent")