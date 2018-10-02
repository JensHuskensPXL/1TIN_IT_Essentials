INCH_IN_METER = 0.0254
PI = 3.14

diameter_wiel = float(input("Diameter wiel in inches: "))

omwenteling_wiel_in_meter = diameter_wiel * PI * INCH_IN_METER
omtrek_in_inches = diameter_wiel * PI
print(omtrek_in_inches)
print(omwenteling_wiel_in_meter)

