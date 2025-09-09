import random

app_run = True

def noppa():
    luku2 = random.randint(1, 6)
    return luku2


while app_run:
    coin = noppa()
    if coin != 6:
        print(coin)
    else:
        print(f"Sinun tulos: {coin}")
        app_run = False