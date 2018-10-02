vertrektijd_uren = int(input("Geef het vertrek uur in: "))
vertrektijd_minuten = int(input("Geef de vertrek minuten in: "))
duur = int(input("geef de duur van de vlucht in (in minuten): "))

aankomstijd_uur_naar_minuten = int(vertrektijd_uren * 60)
aankomstijd_minuut = vertrektijd_minuten + duur + aankomstijd_uur_naar_minuten

aankomstijd_uur = (aankomstijd_minuut // 60) % 24
aankomstijd_minuut = aankomstijd_minuut % 60

print("De vlucht komt aan om ", str(aankomstijd_uur) + " uur " + str(aankomstijd_minuut) + " minuten")