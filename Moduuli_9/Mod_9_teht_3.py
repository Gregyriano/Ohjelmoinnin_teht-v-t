
class Auto:
    def __init__(self,rekisteritunnus,huippunopeus,nopeus=0,kokmatka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kokmatka = kokmatka

    def kiihdyttää(self):
        kiihdytys_run = True
        while kiihdytys_run:
            print(f"{self.nopeus:0.0f}")
            lisänopeus = input("Kirjoita, kuinka paljon haluat kiihdyttää tai paina Enter.")
            if lisänopeus == "":
                kiihdytys_run = False
                continue
            else:
                self.nopeus += int(lisänopeus)
            if self.nopeus <= 0:
                self.nopeus = 0
                print(f"Sinä olet pysähtynyt")
            elif self.nopeus > self.huippunopeus:
                self.nopeus = 142
                print(f"Olet saavuttanut huippunopeuden.")
            print(f"Sinun nopeus on {self.nopeus:0.0f} km/h.")


        return self.nopeus

    def kulje(self, tunnit):
        self.kokmatka = self.kokmatka + tunnit * self.nopeus
        print(f"Kuljettu matka tällä hetkellä on {self.kokmatka:0.0f} km.")
        return self.kokmatka






auto = Auto("ABC-123", 142,0,2000)

print(f"Autollasi on rekisteritunnus {auto.rekisteritunnus:s} ja huippunopeus {auto.huippunopeus:d} km/h.")

auto.kiihdyttää()
auto.kulje(1.5)
