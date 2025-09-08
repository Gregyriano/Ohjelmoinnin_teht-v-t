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


