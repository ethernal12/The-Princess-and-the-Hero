import random
from dataclasses import dataclass

@dataclass
class Baraba:
    x: int
    y: int
    hitrost: int

    def nakljucno_gibanje(self):
        self.x += random.randint(-self.hitrost, self.hitrost)
        self.y += random.randint(-self.hitrost, self.hitrost)

    def trenutna_pozicija(self):
        return self.x, self.y
