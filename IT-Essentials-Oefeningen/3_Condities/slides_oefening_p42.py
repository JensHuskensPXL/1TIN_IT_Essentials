leeftijd = int(input("Geef je leeftijd in: "))

if leeftijd > 50:
    print("Oud")
elif leeftijd > 30:
    print("Ouder")
elif leeftijd > 18:
    print("Jong")
elif leeftijd > 12:
    print("Tiener")
else:
    print("Kind")

