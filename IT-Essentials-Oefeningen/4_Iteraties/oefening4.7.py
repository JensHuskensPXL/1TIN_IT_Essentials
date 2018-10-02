temperatuur = 0
aantal = 0
grootste_temp = 0

for i in range(1,10):
    gemeten_temperatuur = float(input("Geef de gemeten temperatuur om 12u 's middags in: "))
    temperatuur = temperatuur + gemeten_temperatuur
    aantal =+ i
    if gemeten_temperatuur > grootste_temp:
        grootste_temp = gemeten_temperatuur

gemiddelde_temperatuur = temperatuur / aantal

print("De hoogste temperatuur voor deze 10 dagen bedraagd:", grootste_temp)
print("De gemiddelde temperatuur voor deze 10 dagen bedraagd:", gemiddelde_temperatuur)