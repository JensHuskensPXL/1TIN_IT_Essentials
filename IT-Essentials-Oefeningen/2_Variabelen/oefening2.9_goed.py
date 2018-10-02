bedrag = int(input("Hoeveelheid centen: "))

euro_2 = bedrag // 200
rest = bedrag % 200
euro_1 = rest // 100
rest = rest % 100
cent_50 = rest // 50
rest = rest % 50
cent_20 = rest // 20
rest = rest % 20
cent_10 = rest // 10
rest = rest % 10
cent_5 = rest // 5
rest = rest % 5
cent_2 = rest // 2
rest = rest % 2
aantal_een_cent = rest

print(euro_2, "x 2 euro")
print(euro_1, "x 1 euro")
print(cent_50, "x 50 cent")
print(cent_20, "x 20 cent")
print(cent_10, "x 10 cent")
print(cent_5, "x 5 cent")
print(cent_2, "x 2 cent")
print(aantal_een_cent, "x 1 cent")