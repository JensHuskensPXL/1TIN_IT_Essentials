# getal = int(input("Geef een getal in tussen 0 en 10: "))
#
# if getal < 0 or getal > 10:
#     getal = int(input("Geef een getal in tusen 0 en 10: "))

getal = int(input("Geef een getal in tussen 0 en 10: "))

while getal < 0 or getal > 10:
    getal = int(input("Geef een getal in tussen 0 en 10: "))

print("Einde")