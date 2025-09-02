list = []
app_run = True

while app_run == True:
    pipi = input("Anna luku tai lopeta painamalla Enter:")
    if pipi == "":
        app_run = False
    else:
        pipi = int(pipi)
        list.append(pipi)
list.sort(reverse = True)
print(list)
print(list[0:5])