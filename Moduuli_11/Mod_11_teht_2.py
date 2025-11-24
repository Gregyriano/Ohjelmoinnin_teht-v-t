import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kokmatka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kokmatka = kokmatka

    def kiihdyttää(self,muutos):
            self.nopeus += muutos
            if self.nopeus <= 0:
                self.nopeus = 0
                print(f"Auto on pysähtynyt")
            elif self.nopeus > self.huippunopeus:
                self.nopeus = 142
                print(f"Auto on saavuttanut huippunopeuden.")
            print(f"Sinun nopeus on {self.nopeus:0.0f} km/h.")

            return self.nopeus

    def kulje(self, tunnit):
        self.kokmatka = self.kokmatka + tunnit * self.nopeus
        print(f"Kuljettu matka tällä hetkellä on {self.kokmatka:0.0f} km.")
        return self.kokmatka

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapas):
        self.akkukapas = float(akkukapas)
        super().__init__(rekisteritunnus,huippunopeus)

class Polttomoottoriauto(Auto):
    def __init__(self,rekisteritunnus, huippunopeus, tankkoko):
        self.tankkoko = tankkoko
        super().__init__(rekisteritunnus, huippunopeus)


'''
autot = []
for i in range(1,11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100,200)
        autot.append(Auto(rekisteritunnus,huippunopeus))

kilp_matka = 10000
kilp_käynnissä = True

while kilp_käynnissä:
    for auto in autot:
        auto.kiihdyttää(random.randint(-10,15))
        auto.kulje(1)

        if auto.kokmatka > kilp_matka:
            kilp_käynnissä = False

print("Auto, rekisteritunnus, huippunopeus, kuljettu matka")
print("-----------------------------------------")
for auto in autot:
    print(f"{auto.rekisteritunnus}, {auto.huippunopeus}, {auto.kokmatka:0.2f}")
'''

sähköaut = Sähköauto("ABC-15", 180, 52.5)
polttomot = Polttomoottoriauto("ACD-123", 165, 32.3)

sähköaut.kiihdyttää(80)
polttomot.kiihdyttää(160)

print(f"Sähköauto: {sähköaut.kokmatka}")
print(f"Polttomot: {polttomot.kokmatka}")





