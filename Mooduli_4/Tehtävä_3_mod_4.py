numero_lista = []
app_run = True

while app_run == True:
    numero = input("Anna numero tai lopeta painamalla Enter: ")
    numero_lista.append(numero)
    if numero == "":
        numero_lista.remove("")
        app_run = False

mini = str(min(numero_lista))
maksi = str(max(numero_lista))


print(mini)
print(maksi)