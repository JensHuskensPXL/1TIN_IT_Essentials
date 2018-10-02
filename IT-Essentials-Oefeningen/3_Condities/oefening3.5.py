EENHEIDS_PRIJS_ARTIKEL = 11.5
BTW = 0.21

aantal_artikels = int(input("Geef het aantal artikels in dat u wil bestellen: "))

prijs = EENHEIDS_PRIJS_ARTIKEL * aantal_artikels

prijs_zonder_btw = prijs - (prijs * 0.21)

if prijs < 1000:
    print("het bedrag dat u moet betalen is", prijs)
else:
    prijs_met_reductie = prijs_zonder_btw - (prijs_zonder_btw * 0.10)
    print("Het bedragd dat u moet betalen is:", prijs_met_reductie)
