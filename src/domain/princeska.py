from dataclasses import dataclass


@dataclass
class Princeska:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def trenutna_pozicija(self):
        return self.x, self.y

