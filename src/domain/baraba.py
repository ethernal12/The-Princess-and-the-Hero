import random
from dataclasses import dataclass

@dataclass
class Baraba():
    x: int
    y: int
    hitrost: int

    def nakljucno_gibanje(self):

        global nalkjucniX
        global nalkjucniY
        while True:
            nalkjucniX = random.randint(-self.hitrost, self.hitrost)
            nalkjucniY = random.randint(-self.hitrost, self.hitrost)
            naslednjaPozicijaX = self.x + nalkjucniX
            naslednjaPozicijaY = self.y + nalkjucniY
            if naslednjaPozicijaX < 0 or naslednjaPozicijaX > 10:
                print('x')
                nalkjucniX = random.randint(-self.hitrost, self.hitrost)
            elif naslednjaPozicijaY < 0 or naslednjaPozicijaY > 10:
                print('y')
                nalkjucniY = random.randint(-self.hitrost, self.hitrost)
            else:
                break

        self.x += nalkjucniX
        self.y += nalkjucniY

    def trenutna_pozicija(self):
        return self.x, self.y
