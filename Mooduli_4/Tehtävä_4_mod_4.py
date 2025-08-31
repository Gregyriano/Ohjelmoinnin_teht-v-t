import random

koko_luku = random.randint(1, 10)
user_luku = float(input("Kirjoita kokonaisluku: "))

while user_luku != koko_luku:
    if user_luku > koko_luku:
        print("Liian suuri arvaus.")
        user_luku = float(input("Kirjoita kokonaisluku: "))
    elif user_luku < koko_luku:
        print("Liian pieni arvaus.")
        user_luku = float(input("Kirjoita kokonaisluku: "))

print("Oikein!")
