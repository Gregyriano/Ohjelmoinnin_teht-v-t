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


toivottavasti = True
toivottavasti = "Totta"

print(type(toivottavasti))



print("---------------------------0")

 #len, sum, max, min, count
luvut = [1,43,5,6,6,7,8,9,46,65,76,6,465,6,6,6,6,6,6,6,6]
print(len(luvut)) # pituus
print(sum(luvut))
print(min(luvut))
print(max(luvut))
print(luvut.count(6))

print("---------------------------1")

i = 0
while i < len(luvut):
    #print(i)
    print(luvut[i])
    i += 1

print("---------------------------2")

for luku in luvut:
    print(luku)

print("---------------------------3")

for kirjain in "ajsfdlkjadfjl":
    print(kirjain)

print("---------------------------4")

for alkio in [1,2,3,4,5,6,7,8,9]:
    print(alkio)

print("---------------------------5")

for kaupunki in kaupungit:
    kaupungit.sort()
    print(kaupunki)

print("---------------------------6")


for numero in range(5):
    print(numero)

print("---------------------------7")


for n in range(4,80):
    print(n)

print("---------------------------8")

for n in range(50,0,-2):
    print(n)

print("---------------------------9")


pituus = len(luvut)
#luvut = [1,43,5,6,6,7,8,9,46,65,76,6,465,6,6,6,6,6,6,6,6]

for n in range(pituus):
    print(n)
    print(luvut[n])

print("---------------------------10")

for n in range(3):
    print(luvut[n])

print("---------------------------11")

for n in range(3):
    print(kaupungit[n])