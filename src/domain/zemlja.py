from dataclasses import dataclass

from src.domain.baraba import Baraba
from src.domain.hero import Hero
from src.domain.princeska import Princeska


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
            trenutnePozicijeBarab.remove((b.x, b.y))
            b.nakljucno_gibanje()
            x, y = b.x, b.y
            # če naslednja naključna pozicija barabe že obstaja, ponovno izberi pozicijo
            while (x, y) in trenutnePozicijeBarab:
                b.nakljucno_gibanje()
                x, y = b.x, b.y
            trenutnePozicijeBarab.append((x, y))

    # če si izven omejitve zemlje se heroj izriše na drugi strani
    def premakni_heroja(self, dx, dy):
        x = self.hero.x
        y = self.hero.y

        if x + dx > self.sirina:
            self.hero.x = x + dx - self.sirina - 1
        elif x + self.dx < 0:
            self.hero.x = x + dx + self.sirina + 1
        elif y + dy > self.visina:
            self.hero.y = y + dy - self.visina - 1
        elif y + dy < 0:
            self.hero.y = y + dy + self.visina + 1
        else:
            self.hero.premik(dx=dx, dy=dy)
