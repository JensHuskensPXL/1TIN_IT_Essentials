brutoloon = float(input("Geef het brutoloon in: "))

print("brutoloon bedraagd: ", brutoloon)

vakantiegeld = brutoloon / 100 * 5

print("Vakantie geld bedraagd: ", vakantiegeld)

if vakantiegeld < 350:
    jaarlijkse_bijdrage = 350 / 100 * 8
    print("Jaarlijkse bijdrage bedraagd: ", jaarlijkse_bijdrage)
else:
    jaarlijkse_bijdrage = vakantiegeld * 100 * 8
    print("Jaarlijkse bijdrage bedraagd: ", jaarlijkse_bijdrage)