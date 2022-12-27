from dataclasses import dataclass

from src.domain.baraba import Baraba
from src.domain.hero import Hero
from src.domain.princeska import Princeska


@dataclass
class Zemlja:
    sirina: int
    dolzina: int
    hero: Hero
    princeska: Princeska
    barabe: list[Baraba]
