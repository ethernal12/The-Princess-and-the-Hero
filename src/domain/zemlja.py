from dataclasses import dataclass

from src.domain.baraba import Baraba
from src.domain.hero import Hero
from src.domain.princeska import Princeska
import random


@dataclass
class Zemlja:
    sirina: int
    visina: int
    hero: Hero
    princeska: Princeska
    barabe: list[Baraba]
    dx: int
    dy: int

    def premakni_barabo(self):
        trenutnePozicijeBarab = []

        for b in self.barabe:
            trenutnePozicijeBarab.append((b.x, b.y))
        for b in self.barabe:
            # izbriši trenutno pozicijo barabe iz liste barab
            trenutnePozicijeBarab.remove((b.x, b.y))
            # izberi novo pozicijo barabe
            xb, yb = b.nakljucno_gibanje()
            x, y = b.x, b.y
            # prištej treutni poziciji barabe x
            nextx = x + xb
            # prištej treutni poziciji barabe y
            nexty = y + yb
            while (nextx, nexty) in trenutnePozicijeBarab or (
                    nextx < 0 or nextx > self.sirina or nexty < 0 or nexty > self.visina):
                xb, yb = b.nakljucno_gibanje()
                # prištej treutni poziciji barabe x
                nextx = x + xb
                # prištej treutni poziciji barabe y
                nexty = y + yb
                if nextx > self.sirina:
                    print('x je večji od širine')
                    print('trenutni x', nextx)
                    nextx %= self.sirina
                    print('naslednji x', nextx)
                elif nextx < 0:
                    print('x je manjši od širine')
                    print('trenutni x', nextx)
                    nextx = self.sirina + xb
                    print('naslednji x', nextx)
                elif nexty > self.visina:
                    print('y je večji od širine')
                    print('trenutni y', nexty)
                    nexty %= self.visina
                    print('naslednji y', nexty)
                elif nexty < 0:
                    print('y je manjši od širine')
                    print('trenutni y', nexty)
                    nexty = self.visina + yb
                    print('naslednji y', nexty)
            b.premakni_barabo(nextx, nexty)
            trenutnePozicijeBarab.append((nextx, nexty))

    # če si izven omejitve zemlje se heroj izriše na drugi strani
    def premakni_heroja(self, dx, dy):
        x = self.hero.x
        y = self.hero.y
        if x + dx > self.sirina:
            self.hero.x = 0
        elif x + dx < 0:
            self.hero.x = self.sirina + dx
        elif y + dy > self.visina:
            self.hero.y = 0
        elif y + dy < 0:
            self.hero.y = self.visina + dy
        else:
            self.hero.premik(dx=dx, dy=dy)
