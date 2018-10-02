gewicht_appel = int(input("Geef het gewicht van een appel in: "))

for i in range(1,101):
    gram = i * gewicht_appel
    print(i, "appel(s) =", gram, "gr")