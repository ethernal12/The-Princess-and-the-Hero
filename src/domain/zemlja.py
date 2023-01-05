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

