class Auto:
    def __init__(self,rekisteritunnus,huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus

auto = Auto("ABC-123", 142)

print(f"Autollasi on rekisteritunnus {auto.rekisteritunnus:s} ja huippunopeus {auto.huippunopeus:d} km/h.")

