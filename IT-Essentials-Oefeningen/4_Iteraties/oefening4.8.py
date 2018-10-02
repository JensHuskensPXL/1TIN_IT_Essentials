aantal_renners = int(input("geef het aantal renners in: "))
tijd = 0
percentage_snelste_renners = 0

for i in range(0,aantal_renners):
    inschrijvings_nummer = str(input("Geef het inschrijvingsnummer van de renner in: "))
    if "-" in inschrijvings_nummer:
        print("lol")
    else:
        tijd_in_seconden = int(input("Geef de tijd van de renner in seconden weer: "))
    print()