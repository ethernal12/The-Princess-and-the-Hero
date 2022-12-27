from src.domain.baraba import Baraba
from src.domain.hero import Hero
from src.domain.princeska import Princeska
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
        stBarab = self.level * 9

        sirina = 10 * self.level
        visina = 10 * self.level

        # generiraj vse mozne kombinacije matrice
        moznePozicije = [(x, y) for x in range(sirina) for y in range(visina)]

        for i in range(stBarab):
            # izberi med pozicijami, ki so še na voljo
            x, y = random.choice(moznePozicije)
            barabe.append(
                Baraba(
                    x=x,
                    y=y,
                    hitrost=2)
            )
            # vsakic odstrani pozicijo barabe iz moznih pozicij
            moznePozicije.remove((x, y))
        # izberi pozicije za heroja in princesko
        xh, yh = random.choice(moznePozicije)
        moznePozicije.remove((xh, yh))
        xp, yp = random.choice(moznePozicije)
        moznePozicije.remove((xp, yp))

        self.zemlja = Zemlja(
            sirina=10 * self.level,
            dolzina=10 * self.level,
            hero=Hero(
                x=xh,
                y=yh),
            princeska=Princeska(
                x=xp,
                y=yp
            ),
            barabe=barabe
        )

    def draw_game(self):
        for y in range(self.zemlja.dolzina + 1):
            for x in range(self.zemlja.sirina + 1):
                flag = False
                for b in self.zemlja.barabe:
                    if b.x == x and b.y == y:
                        print('\033[31mB\033[0m ', end='')
                        flag = True
                        break
                if flag:
                    continue
                if x == self.zemlja.hero.x and y == self.zemlja.hero.y:
                    print('\033[32mH\033[0m ', end='')
                elif x == self.zemlja.princeska.x and y == self.zemlja.princeska.y:
                    print('\u2665', end='')
                else:
                    print('. ', end='')
            print()

    # premik heroja z inputi
    def input(self):
        global dx
        global dy
        x, y = self.zemlja.hero.trenutna_pozicija()
        while True:

            dx = int(input("Vnesi dx med +2 in -2, premik mora biti v mejah zemlje!: "))
            print(x - (-dx))
            print(x - (-dx) >= 0)
            if dx in [1, 2, -1, -2, 0] and (x + dx <= self.zemlja.sirina and x - (-dx) >= 0):
                break
        while True:

            dy = int(input("Vnesi dy med +2 in -2, premik mora biti v mejah zemlje!: "))
            print(y + dy, 'dy')
            print(y + dy < self.zemlja.dolzina or y - (-dy) > 0)
            if dy in [1, 2, -1, -2, 0] and (y + dy <= self.zemlja.dolzina and y - (-dy) >= 0):
                break
        self.zemlja.hero.premikanje(dx=dx, dy=dy)

    def premakni_barabo(self):
        sirina = 10 * self.level
        visina = 10 * self.level

        # generiraj vse mozne kombinacije matrice
        trenutnePozicijeBarab = []
        naKoncu = []

        for b in self.zemlja.barabe:
            trenutnePozicijeBarab.append((b.x, b.y))

        for b in self.zemlja.barabe:
            print(b.x, b.y, 'trenutna baraba v for')
            # ostrani x,y pozicijo trenutne barabe
            trenutnePozicijeBarab.remove((b.x, b.y))
            # izvedni naključno gibanje barabe
            b.nakljucno_gibanje()
            # dobi trenutno pozicijo barabe
            x, y = b.trenutna_pozicija()
            # če je premik trenutne barabe na pozicijo katerekoli
            # druge barabe, ponovi gibanje barabe dokler temu ni tako
            while (x, y) in trenutnePozicijeBarab:
                #print(str((x, y)) + 'pozicija že obstaja za drugo barabo')
                #print(trenutnePozicijeBarab)
                b.nakljucno_gibanje()
                x, y = b.trenutna_pozicija()
                #print('ponovna izbira pozicije barabe je:' + str((x, y)))

        # for b in self.zemlja.barabe:
        #     naKoncu.append((b.x, b.y))
        # print(naKoncu, 'nakoncu')
        # if len(set(naKoncu)) == len(naKoncu):
        #     print("Barabe so vsaka na svojem mestu.")
        # else:
        #     print("Baraba je na drugi barabi.")

    def end_game(self):
        # trenutna pozicija heroja
        xh, yh = self.zemlja.hero.trenutna_pozicija()
        xp, yp = self.zemlja.princeska.trenutna_pozicija()
        for b in self.zemlja.barabe:
            # trenutna pozicija barab
            xb, yb = b.trenutna_pozicija()
            if yh == yb and xb in range(xh - 1, xh + 2) :
                print('Heroj ujet, princeska zaman čaka svojega junaka...')
                return True
            elif xh == xb and yb in range(yh - 1, yh + 2) :
                print('Heroj ujet, princeska zaman čaka svojega junaka...')
                return True
            elif xb == xp and yb == yp:
                print('Barbaba ujela princesko...')
                return True
            elif xh == xp and yh == yp :
                print('Prineska rešena in pade v objem pogumnemu heroju..')
                return True
