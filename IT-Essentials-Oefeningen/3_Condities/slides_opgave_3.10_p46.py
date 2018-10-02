gewicht = int(input("Geef het gewicht van de bagage in (in kg): "))

if gewicht > 20:
    print("Er moet een toeslag van €25 betaald worden voor bagage die te zwaar is")
elif gewicht < 20:
    print("Goede rijs!")
elif gewicht == 20:
    print("Poeh, Dat gewicht is precis goed!")