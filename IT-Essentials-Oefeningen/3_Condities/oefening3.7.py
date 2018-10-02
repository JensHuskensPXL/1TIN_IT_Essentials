examen1 = int(input("Geef het resultaat van het 1ste examen in op 20: "))
examen2 = int(input("Geef het resultaat van het 2de examen in op 20: "))
examen3 = int(input("geef het resultaat van het 3de examen in op 20: "))

totaal_examen = examen1 + examen2 + examen3

percentage = totaal_examen / 60 * 100

if percentage < 60:
    print("Onvoldoende")
elif percentage < 70:
    print("voldoende")
elif percentage < 80:
    print("onderscheiding")
elif percentage < 90:
    print("Grote onderscheiding")
else:
    print("Grootste onderscheiding")