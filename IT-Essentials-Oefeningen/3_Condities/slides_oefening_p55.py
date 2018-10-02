lengte = float(input("Geef hier je lengte in ( in meter): "))
gewicht = float(input("Geef hier je gewicht in (in kg): "))

bmi = gewicht / (lengte * lengte)

if bmi < 18:
    print("Ondergewicht")
elif bmi < 25:
    print("OK")
elif bmi < 30:
    print("overgewicht")
elif bmi < 40:
    print("obesitas")
else:
    print("ziekelijk overgewicht")