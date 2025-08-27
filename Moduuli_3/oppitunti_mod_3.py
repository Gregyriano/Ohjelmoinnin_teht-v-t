import random

suorita_silmikka = True

while suorita_silmikka:
    suorita_silmikka = False
    print("totta")
    print("on")

print("silmikan suoritus loppui")

toistojen_lkm = 10
i = 0

while i < toistojen_lkm:
    print(f"iteroiva silmukka, i:n arvo: {i} ")
    i = i + 1
    #i += 1, eli periaatteessa sama homma kuin edellinen rivi
print(f"i:n arvo lopuksi: {i}")

app_running = True
# "main loop"
while app_running:
    command = input("komento> ")
    print(f"komentosi oli: {command}")
    if command == "lopeta":
        app_running = False
    elif command == "on":
        luku1 = float(input("Anna ensimmäinen luku: "))
        luku2 = float(input("Anna toka luku: "))
        tulos_yhteenlasku = luku1 + luku2
        print(f"Yhteenlaskutoimituksen tulos: {tulos_yhteenlasku:0.0f}")

#kolikonheitto simulaattori

n = 10000
i = 0
kolikko_pystyssä_lkm = 0
while i < n:
    i += 1
    sattunaisluku = random.randint(0,1000)
    print(f"arvottu luku: {sattunaisluku} ")
    if sattunaisluku < 500:
        print("Kruuna")
    elif sattunaisluku > 500:
        print("Klaava")
    else:
        print("Kolikko jäi pystyyn")
        kolikko_pystyssä_lkm += 1
print(f"Kolikko jäi pystyyn {kolikko_pystyssä_lkm} kertaa.")