import random

tulos = 0
N = int(input("Anna joku numero."))

for n in range(1,N):
    kuutio = random.randint(1,6)
    tulos += kuutio
    #print(kuutio)

print(f"{tulos:.0f}")