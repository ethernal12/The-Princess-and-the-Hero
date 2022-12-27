from src.domain.baraba import Baraba
from src.domain.hero import Hero
from src.domain.zemlja import Zemlja
import random
import sys


class Console():
    def __init__(self):
        self.zemlja = None
        self.level = 1
        self.runda = 1

    def new_game(self):
        barabe: list[Baraba] = []
        stBarab = self.level * 2
        vrste =10 * self.level
        stolpi =10 * self.level

        # generiraj vse mozne kombinacije matrice
        moznePozicije = [(x,y) for x in range(vrste) for y in range(stolpi)]


        for i in range(stBarab):
            # izberi med številkami, ki so še na voljo v naboru številk
            x, y = random.choice(moznePozicije)
            barabe.append(
                Baraba(
                    x=x,
                    y=y,
                    hitrost=2)
            )
            # vsakic odstrani pozicijo iz moznih pozicij
            moznePozicije.remove((x, y))

        x, y = random.choice(moznePozicije)
        self.zemlja = Zemlja(
            sirina=10 * self.level,
            dolzina=10 * self.level,
            hero=Hero(
                x=x,
                y=y),
            barabe=barabe
        )
        # vsakic odstrani pozicijo iz moznih pozicij
        moznePozicije.remove((x, y))
    def draw_game(self):
        for y in range(self.zemlja.dolzina + 1):
            for x in range(self.zemlja.sirina + 1):
                flag = False
                for b in self.zemlja.barabe:
                    if b.x == x and b.y == y:
                        print('B ', end='')
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
        # omejitev gibanje heroja na sirino, dolzino zemlje
        x, y = self.zemlja.hero.trenutna_pozicija()

        if x + dx > self.zemlja.sirina or x - (-dx) < 0:
            print('Premik heroja izven sirine zemlje')
        elif y + dy > self.zemlja.dolzina or y - (-dy) < 0:
            print('Premik heroja izven dolžine zemlje')
        else:
            self.zemlja.hero.premikanje(dx=dx, dy=dy)

    def end_game(self):
        # trenutna pozicija heroja
        xh, yh = self.zemlja.hero.trenutna_pozicija()
        for b in self.zemlja.barabe:
            # trenutna pozicija barab
            xb, yb = b.trenutna_pozicija()
            if yh == yb and xb in range(xh - 3, xh + 4):
                print('Baraba ujeta, princessa rešena in igre konec...')
                sys.exit()
            elif xh == xb and yb in range(yh - 3, yh + 4):
                print('Baraba ujeta, princessa rešena in igre konec...')
                sys.exit()
