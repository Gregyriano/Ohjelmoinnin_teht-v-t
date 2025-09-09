import math

halk1 = float(input("Anna ensimmäisen pizzan halkaisija: "))
hin1 = float(input("Anna ensimmäisen pizzan hinta: "))

halk2 = float(input("Anna toisen pizzan halkaisija: "))
hin2 = float(input("Anna toisen pizzan hinta: "))

def hyeta(halk,hin):
    # muunnan sentimetrit metreiksi
    pipka = halk / 100
    #lasken pihta-ala
    ploshad = math.pi * (pipka/2) * (pipka/2)
    tsena_za_metr = hin / ploshad
    print(tsena_za_metr)
    return tsena_za_metr

if hyeta(halk1,hin1) < hyeta(halk2,hin2):
    print("Ensimmäisen pizzan hinta on edullisempi")
else:
    print("Toisen pizzan hinta on parempi")

