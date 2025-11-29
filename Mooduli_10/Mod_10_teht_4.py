class Hissi:

    def __init__(self,alin, ylin,numero):
        self.alin = alin
        self.ylin = ylin
        self.nykykerros = alin
        self.numero = numero

    def kerros_alas(self):
        self.nykykerros -= 1
        if self.nykykerros < self.alin or self.nykykerros == self.alin:
            self.nykykerros = self.alin
        print(f"Hissi {self.numero}: on kerroksessa {self.nykykerros}")
        return

    def kerros_ylös(self):
        self.nykykerros += 1
        if self.nykykerros > self.ylin or self.nykykerros == self.ylin:
            self.nykykerros = self.ylin
        print(f"Hissi {self.numero}: on kerroksessa {self.nykykerros}")
        return

    def siirry_kerrokseen(self, kerros):
        self.kerros = kerros
        while self.nykykerros != self.kerros:
            if self.nykykerros < self.kerros:
                self.kerros_ylös()
            else:
                self.kerros_alas()
        return

class Talo:

    def __init__(self, alin, ylin, his_lkm):

        self.hissit = []
        self.alin = alin
        self.ylin = ylin
        self.his_lkm = his_lkm

        for i in range(his_lkm):
            hissi = Hissi(alin, ylin,i+1)
            self.hissit.append(hissi)
            print(f"Hissi {i + 1} luotu (kerrokset {alin}–{ylin})")

    def aja_hissiä(self,hissi_numero, kohdekerros):

        hissi = self.hissit[hissi_numero-1]
        print(f"\nAjetaan hissiä {hissi.numero} kerrokseen {kohdekerros}")
        hissi.siirry_kerrokseen(kohdekerros)

    def palohalytys(self):

        print("\n!!! PALOHÄLYTYS – Kaikki hissit alas !!!\n")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin)





Padik = Talo(1, 20, 3)

Padik.aja_hissiä(1, 10)
Padik.aja_hissiä(3, 5)

Padik.palohalytys()


