import random

# kaikkien pistojen määrä
N = float(input("Anna suuri luku: "))
n = i = 0

while i < N:
    i += 1
    # arvotaan satunnainen piste koordinatistoon
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f"Arvotuu piste: {x}, {y}")

    if x*x + y*y < 1:
        n += 1
    # jos ehto on totta, kasvata n-laskurin arvoa

print(f"Pi:n liukuluku ≈ {4 * n / N:0.4f}.")
