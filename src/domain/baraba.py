import random
from dataclasses import dataclass

from src.app.console import Console


@dataclass
class Baraba():
    x: int
    y: int
    hitrost: int

    def nakljucno_gibanje(self):

        console = Console()
        # pokličemo new_game v Console class
        console.new_game()
        # Dostopimo do zemlja instance in atributa sirina
        sirina = console.zemlja.sirina
        visina = console.zemlja.visina

        global nalkjucniX
        global nalkjucniY
        # če izbere baraba naključno smer izven omejitev zemlje, ponovno izbere drugo naključno smer...
        while True:
            nalkjucniX = random.randint(-self.hitrost, self.hitrost)
            nalkjucniY = random.randint(-self.hitrost, self.hitrost)
            naslednjaPozicijaX = self.x + nalkjucniX
            naslednjaPozicijaY = self.y + nalkjucniY

            if naslednjaPozicijaX < 0 or naslednjaPozicijaX > sirina:

                nalkjucniX = random.randint(-self.hitrost, self.hitrost)

            elif naslednjaPozicijaY < 0 or naslednjaPozicijaY > visina:

                nalkjucniY = random.randint(-self.hitrost, self.hitrost)
            else:
                break

        self.x += nalkjucniX
        self.y += nalkjucniY

    def trenutna_pozicija(self):
        return self.x, self.y
