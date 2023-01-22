import random
from dataclasses import dataclass


@dataclass
class Baraba:
    x: int
    y: int
    hitrost: int

    # TODO: pODREJENI ELEMENTI NE SMEJO PRI INICIALIZACIJI ALI PRI RUNTIMU VEDETI ZA VIŠNE ELEMENTE NITI NJIHOVE INFORMACIJE
    # NALJKUČNI X = NONE

    def nakljucno_gibanje(self):
        global nalkjucniX
        global nalkjucniY
        nalkjucniX = random.randint(-self.hitrost, self.hitrost)
        nalkjucniY = random.randint(-self.hitrost, self.hitrost)
        return nalkjucniX, nalkjucniY

    def premakni_barabo(self, xb, yb):
        self.x = xb
        self.y = yb
