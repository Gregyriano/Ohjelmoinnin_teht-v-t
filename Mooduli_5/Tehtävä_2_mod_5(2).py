list = []
n = input("Syötä numero tai lopeta painamalla Enter:")

while n != "":
    print(n)
    list.append(int(n))
    n = input("Syötä numero tai lopeta painamalla Enter:")

list.sort(reverse = True)
print(list)
print("")
viisi_suurinta = list[:5]
