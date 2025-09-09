
def convertor(gallons):

    litrat = gallons * 3.785

    return litrat

galli = float(input("Syötä nestegallonoin määrä: "))

while galli > 0:
    pipki  = convertor(galli)
    print("Sinun bensiini määrä litroina:", pipki)
    galli = float(input("Syötä nestegallonoin määrä: "))
else:
    print("Väärä syöte:")
