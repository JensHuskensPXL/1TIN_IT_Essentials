#Oefening 2.2 De toegangsprijs voor een dierentuin bedraagt 11 euro
#voor volwassenen en 6 euro voor kinderen onder de 12 jaar.
# Maak een programma dat het aantal volwassenen en kinderen
# inleest via toetsenbord en dat de totale prijs berekent
# en afdrukt.

PRIJS_VOLWASSENEN = 12.0
PRIJS_KINDEREN = 6.0
PRIJS_EENHEID = "€"

aantal_volwassenen = int(input("Aantal Volwassenen: "))
aantal_kinderen = int(input("Aantal Kinderen: "))

toegangsprijs = PRIJS_EENHEID + str(PRIJS_VOLWASSENEN * aantal_volwassenen + PRIJS_KINDEREN * aantal_kinderen)

print("De totale prijs is", toegangsprijs)