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
        i = 0

        for b in self.barabe:
            trenutnePozicijeBarab.append((b.x, b.y))
        for b in self.barabe:
            i += 1
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
                    nextx %= self.sirina
                elif nextx < 0:
                    nextx += self.sirina
                elif nexty > self.visina:
                    nexty %= self.visina
                elif nexty < 0:
                    nexty += self.visina
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
