# gewicht_aarde = int(input("Geef je gewicht in: "))
#
# for i in ("aarde", "maan", "jupiter", "mars"):
#     if i == "aarde":
#         factor = 1
#     elif i == "maan":
#         factor = 0.165
#     elif i == "jupiter":
#         factor = 2.537
#     else:
#         factor = 0.378
#     gewicht = factor * gewicht_aarde
#     print(i + ":", gewicht)

maan = float(input("Geef de percentag gewicht van de maan tov aarde nl 16.5: "))
jupiter =
mars =

for i in range(50,125,5):
    print("Aarde:", i)
    print("Maan:", i * maan / 100)
    print("Jupiter:" , i * jupiter / 100)
    print("Mars:", i * mars / 100)
    print()