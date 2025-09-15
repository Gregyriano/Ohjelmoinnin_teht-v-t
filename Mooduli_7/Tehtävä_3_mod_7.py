
lentoasemat = {
    "EFRO" : "Rovaniemi Airport",
    "EFTP" : "Tampere–Pirkkala Airport",

}

def lisätään_nimi():

    koodi = input("Kirjoita aseman koodi: ")
    nimi = input("Kirjoita lentoaseman nimi: ")

    if koodi in lentoasemat:
        print("Lentoasema on jo listalla.")
    else:
        lentoasemat[koodi] = nimi

    return lentoasemat

n = input("Kirjoita 'Syöttää' jos haluat lisätä lentoasema, 'hakea' jos haluat tarkistaa lentoasema listalla tai paina Enter, jos haluat lopeta: ")

while n != "":
    if n == "Syöttää":
        lisätään_nimi()
        n = input("Kirjoita 'syöttää' jos haluat lisätä lentoasema, 'hakea' jos haluat tarkistaa lentoasema listalla tai paina Enter, jos haluat lopeta: ")
    elif n == ("hakea"):
        koodi_kysy = input("Kirjoita lentoaseman koodi: ")
        if koodi_kysy in lentoasemat:
            print(f"Vaastava lentoasema: {lentoasemat[koodi_kysy]}")
            n = input("Kirjoita 'syöttää' jos haluat lisätä lentoasema, 'hakea' jos haluat tarkistaa lentoasema listalla tai paina Enter, jos haluat lopeta: ")
        else:
            print("Asema ei ole listalla.")
            n = input("Kirjoita 'syöttää' jos haluat lisätä lentoasema, 'hakea' jos haluat tarkistaa lentoasema listalla tai paina Enter, jos haluat lopeta: ")

    else:
        print("Väärä syöte.")
        n = input("Kirjoita 'syöttää' jos haluat lisätä lentoasema, 'hakea' jos haluat tarkistaa lentoasema listalla tai paina Enter, jos haluat lopeta: ")

print(lentoasemat)




