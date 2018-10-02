leeftijd = int(input("geef je leeftijd in: "))

print("Leeftijd:", leeftijd)

if leeftijd < 12:
    print("Lidgeld bedraagd 6 euro ")
elif leeftijd < 18:
    print("lidgeld bedraagd 12.5 euro")
else:
    print("Lidgeld bedraagd 25 euro")