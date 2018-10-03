geheel_getal = int(input("Geef een geheel getal in: "))

for i in range(1,21):
    tabel = i * geheel_getal
    print(i, "x", geheel_getal, "=", tabel)

# print("{:2} x {:2} = {:4}".format(i,geheel_getal, tabel)) 