

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(self.nimi)

class Kirja(Julkaisu):
    def __init__(self,nimi,kirjoittaja,siv_lkm):
        self.kirjoittaja = kirjoittaja
        self.siv_lkm = siv_lkm
        super().__init__(nimi)
    def tulosta_tiedot(self):
        print(f"Kirhan nimi on {self.nimi}, kirjoittaja on {self.kirjoittaja} ja sivujen lukumäärä on {self.siv_lkm}")

class Lehti(Julkaisu):
    def __init__(self,nimi,päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)
    def tulosta_tiedot(self):
        print(f"Lehden nimi on {self.nimi} ja päätoimittaja on {self.päätoimittaja}")


lehti = Lehti("Aku Ankka","Aki Hyppä")
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", "200")

lehti.tulosta_tiedot()
kirja.tulosta_tiedot()