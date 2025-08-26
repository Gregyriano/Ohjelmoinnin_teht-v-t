import math

ympyrän_säte_str = input("Kirjoita ympyrän säte:")

ympyrän_säte = float(ympyrän_säte_str)

ympyrän_pinta_ala = math.pi * ympyrän_säte * ympyrän_säte

print(f"Tämä on sinun ympyrän pinta-ala: {ympyrän_pinta_ala:.2f}")
