eka = input("Kirjoita kokonaisluku: ")

toka = input("Kirjoita kokonaisluku: ")

kolmas = input("Kirjoita kokonaisluku: ")

lukujen_summa = float(eka) +float(toka) + float(kolmas)

lukujen_keskiarvo = (float(eka) + float(toka) + float(kolmas)) / 3

lukujen_tulo = int(eka) * int(toka) * int(kolmas)

print(f"Tämä on lukujen summa: {lukujen_summa:0.0f}")

print(f"Tämä on lukujen tulo: {lukujen_tulo:0.0f}")

print(f"Tämä on lukujen keskiarvo: {lukujen_keskiarvo:0.2f}")