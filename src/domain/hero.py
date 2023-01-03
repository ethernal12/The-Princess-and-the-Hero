from dataclasses import dataclass


@dataclass
class Hero:
    x: int
    y: int
    tocke: int = 0


    def premik(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
