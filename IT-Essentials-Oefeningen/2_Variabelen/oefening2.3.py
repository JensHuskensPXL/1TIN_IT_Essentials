#Oefening 2.3 Voer je lengte (in m) en gewicht (in kg) in via het
# toetsenbord. Bereken je BMI en druk af. Je BMI wordt als volgt
# berekend:  gewicht/(lengte×lengte) .

lengte = float(input("Voer lengte in in meter: "))
gewicht = float(input("Voer gewicht in in KG: "))


berekening_bmi = gewicht / (lengte * lengte)
print(berekening_bmi)