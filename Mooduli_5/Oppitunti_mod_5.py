kaupungit = ["Espoo", "Vantaa", "Helsinki", "Joensuu", "Lappeenranta"]

print(kaupungit[:3])
print(kaupungit[-1])

kaupungit.append("Uusi nimi")
print(kaupungit)

if "Espoo" in kaupungit:
    print(f"Espoo Kaupunki löytyi!")
    kaupungit.remove("Espoo")
    print(kaupungit)

kaupungit.insert(0,"Tampere")
print(kaupungit)

monesko = kaupungit.index("Helsinki")

print(monesko)

lisää_kaupunkeja = ["Oulu", "Kotka", "Sipöö"]
kaupungit.extend(lisää_kaupunkeja)
print(kaupungit)

kaupungit[8] = "Sipoo"
print(kaupungit)


hedelmiä = ["appelsiini","Appelsiini", "Greippi", "greippi", "Banaani" ]
numerolista = [23,23,4,6,4,3,254,3425,43554,3]

hedelmiä.sort()
print(hedelmiä)

numerolista.sort(reverse = True)
print(numerolista)


viikonpäivät = {"maanantai", "Tiistai"}
print(viikonpäivät)
