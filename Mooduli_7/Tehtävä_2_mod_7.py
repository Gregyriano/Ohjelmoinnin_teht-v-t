
n = input("Anna nimi: ")
nimet = set()

while n != "":
    if n in nimet:
        print('Aiemmin syötetty nimi.')
        n = input("Anna nimi: ")
    else:
        print("uusi nimi!")
        nimet.add(n)
        n = input("Anna nimi: ")

for nimi in nimet:
    print(nimi)




