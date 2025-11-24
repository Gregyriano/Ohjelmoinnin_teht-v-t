

class Hissi:

    def __init__(self,alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykykerros = alin

    def kerros_alas(self):
        self.nykykerros -= 1
        if self.nykykerros < self.alin or self.nykykerros == self.alin:
            self.nykykerros = self.alin
            print("Sinä olet alimmassa kerroksessa.")
        print(f"Sinä olet kerroksessa {self.nykykerros}")
        return

    def kerros_ylös(self):
        self.nykykerros += 1
        if self.nykykerros > self.ylin or self.nykykerros == self.ylin:
            self.nykykerros = self.ylin
            print("Sinä olet ylimmässä kerroksessa.")
        print(f"Sinä olet kerroksessa {self.nykykerros}")
        return

    def siirry_kerrokseen(self, kerros):
        self.kerros = kerros
        while self.nykykerros != self.kerros:
            if self.nykykerros < self.kerros:
                self.kerros_ylös()
            else:
                self.kerros_alas()
        return

h = Hissi(-5,10)

h.siirry_kerrokseen(5)
h.siirry_kerrokseen(-5)
