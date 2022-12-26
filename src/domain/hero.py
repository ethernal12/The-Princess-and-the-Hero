class Hero:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.tocke = 0

    def premikanje(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy