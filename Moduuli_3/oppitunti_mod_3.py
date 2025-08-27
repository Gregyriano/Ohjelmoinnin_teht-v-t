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
elif command == "laskukone"
    luku1 = float(input("Anna ensimmäinen luku: "))
    luku2 = float(input("Anna toka luku: "))
    tulos_yhteenlasku = luku1 + luku2
    print("Yhteenlaskutoimituksen tulos: ") + str(tulos_yhteenlasku)

#kolikonheitto simulaattori