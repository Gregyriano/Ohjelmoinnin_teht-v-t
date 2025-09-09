import random

lista = [1,2,3,4,5,6]

print(lista)

monikko = (1,2,3,4,5,6)
print(monikko)

monikko2 = 1,2,3,4,5,6
print(monikko2)

monikko3 = (1,2, "ulla", (3,4), 88)
print(monikko3)

print(lista[0])
print(monikko[0])

lista[0] = 0
print("muokattulista",lista)


#viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
#järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
#viikonpäivä = viikonpäivät[järjestysnumero-1]
#print (f"{järjestysnumero}. viikonpäivä on {viikonpäivä}.")

sanat = ("eka","toka","kolmas","viides0","kolmas","neljäs","viides")

for sana in sanat:
    print(sana)
    if sana == "kolmas":
        print("Sana kolmas löytyi!!!")
if "viides" in sanat:
    print("sana viides löytyi")

hedelmät = ("lime","sitruuna", "ananas")
#tämä on sama asia - (eka,toka,kolmas) = ("lime","sitruuna","ananas")
(eka,toka,kolmas) = hedelmät
print("monikko purettu muuttujiin, tässä eka:", eka )

def tulosta_monikko(hedelmät):
    for i in hedelmät:
        print(i)

tulosta_monikko(hedelmät)

def heitä():
    ekä = random.randint(1,6)
    toka = random.randint(1,6)
    print(f"nopista tuli {ekä} ja {toka}")
heitä()

def heitä2():
    ekä, toka = random.randint(1,6),random.randint(1,6)
    print(f"nopista tuli {ekä} ja {toka}")
heitä2()

def heitä3():
    ekä, toka = random.randint(1,6),random.randint(1,6)
    return ekä, toka

noppa1, noppa2 = heitä3()
print("Funktiolla heitä3 palautui arvot",noppa1,noppa2)

oppilaat = \
{
    "Aappeli": 25,
    "Bertta": 52,
    "Rooni": 49,
    "Daniel": 23
}
print(oppilaat)

print(oppilaat.items())

print((oppilaat.keys()))

print(oppilaat.values())

for o in oppilaat:
    print(o)

avain = "Aappeli"
oppilaat[avain]
print("etsitään avaimella Aappeli hänen ikä:",oppilaat[avain])
print("Bertan ikä:", oppilaat["Bertta"])

for o in oppilaat:
    print(f"'Oppilaan nimi on {o} ja ikä on {oppilaat[o]}")

#nimi = input("Anna nimi jota etsin sanakirjassa: ")
#if nimi in oppilaat:
 #   ikä = oppilaat[nimi]
#    print(f"Nimi {nimi} löytyi!!!!!!")
 #   print(f"Hänen ikä on {ikä}")
#else:
   # print(f"Nimi {nimi} ei löyty")

yhteystiedot = \
{
    "Aappeli": {
        "puh": "050228322",
        "osoite" : "Ul Pushkina"
    },
    "Bertta": {
        "puh" : "050322228",
        "osoite" : "UL Koroleva"
    },
    "Rooni": {
        "puh" : "05014887",
        "osoite" : "UL Govna"
    }
}
print("Aappelin puhelinnumero: ", yhteystiedot["Aappeli"]["puh"])