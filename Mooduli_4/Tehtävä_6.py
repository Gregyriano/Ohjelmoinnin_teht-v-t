import random

# kaikkien pistojen määrä
N = 1000
i = 0
while i < N:
    i += 1
    # arvotaan satunnainen piste koordinatistoon
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f"Arvotuu piste: {x}, {y}")
    # TODO: testaa, toteuttaako piste epäyhtälön x*x + y*y < 1
