from src.domain.baraba import Baraba
from src.domain.hero import Hero
from src.domain.zemlja import Zemlja
import random


class Console():
    def __init__(self):
        self.zemlja = None
        self.level = 1

    def new_game(self):
        barabe: list[Baraba] = []
        stBarab = self.level * 2

        for i in range(stBarab):
            barabe.append(
                Baraba(
                    x=random.randint(0, 10 * self.level),
                    y=random.randint(0, 10 * self.level),
                    hitrost=2)
            )

        self.zemlja = Zemlja(
            sirina=10 * self.level,
            dolzina=10 * self.level,
            hero=Hero(
                x=random.randint(0, 10 * self.level),
                y=random.randint(0, 10 * self.level)),
            barabe=barabe
        )

    def draw_game(self):
        for y in range(self.zemlja.dolzina+1):
            for x in range(self.zemlja.sirina+1):
                flag = False
                for b in self.zemlja.barabe:
                    if b.x == x and b.y == y:
                        print('B ',end='')
                        flag = True
                        break
                if flag:
                    continue
                if x == self.zemlja.hero.x and y == self.zemlja.hero.y:
                    print('H ', end='')
                else:
                   print('. ', end='')
            print()


    def input(self):
        dx = int(input("Vnesi dx: "))
        dy = int(input("Vnesi dy: "))
        self.zemlja.hero.premikanje(dx=dx, dy=dy)

        for b in self.zemlja.barabe:
            b.nakljucno_gibanje()
