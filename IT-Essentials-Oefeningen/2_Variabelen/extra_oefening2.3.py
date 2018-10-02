INCH_IN_METER = 0.0254
PI = 3.14

diameter_wiel = float(input("Diameter wiel in inches: "))
opgegeven_meter = float(input("aantal meters afgelegd: "))

omwenteling_wiel_in_meter = diameter_wiel * PI * INCH_IN_METER
hoeveel_omwentelingen_per_meter = opgegeven_meter / omwenteling_wiel_in_meter
print(hoeveel_omwentelingen_per_meter)