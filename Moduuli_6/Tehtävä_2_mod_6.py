import random

app_run = True

pipki = int(input("Syötä tahkojen yhteismäärä: "))
def noppa(maksimitahkojen_määrä):

    luku2 = random.randint(1, maksimitahkojen_määrä)
    return luku2


while app_run:
    coin = noppa(pipki)
    if coin != pipki:
        print(coin)
    else:
        print(f"Sinun tuloksesi: {coin}")
        app_run = False