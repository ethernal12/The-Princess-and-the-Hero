from dataclasses import dataclass

from src.domain.baraba import Baraba
from src.domain.hero import Hero

@dataclass
class Zemlja:
    sirina: int
    dolzina: int
    hero: Hero
    barabe: list[Baraba]
