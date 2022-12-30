from dataclasses import dataclass

import random
import sys


@dataclass
class Console():
    def __init__(self):

        self.zemlja = None
        self.level = 1
        self.maxKoraki = 10
        self.stetjeKorakov = 0
        self.rezultat = 0
        self.preostaliKoraki = 10

    def new_game(self):
        barabe: list[Baraba] = []
        stBarab = self.level * 2
        sirina = 15 - self.level
        visina = 15 - self.level
        self.preostaliKoraki = 10

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
            sirina=sirina,
            visina=visina,
            hero=Hero(
                x=xh,
                y=yh),
            princeska=Princeska(
                x=xp,
                y=yp),
            barabe=barabe
        )

    def draw_game(self):
        print('draw game')
        print(f'\033[1m\033[33m{self.level} LEVEL\033[0m')
        print(f'\033[1m\033[33mSCORE {self.rezultat} \033[0m')
        print('---------')
        print(f'\033[1m\033[33mPreostali koraki {self.preostaliKoraki} \033[0m')
        print('-------------------')
        for y in range(self.zemlja.visina + 1):
            for x in range(self.zemlja.sirina + 1):
                flag = False
                for b in self.zemlja.barabe:
                    if b.x == x and b.y == y:
                        print('\033[91mB\033[0m ', end='')
                        flag = True
                        break
                if flag:
                    continue
                if x == self.zemlja.hero.x and y == self.zemlja.hero.y:
                    print('\033[92mH\033[0m ', end='')
                elif x == self.zemlja.princeska.x and y == self.zemlja.princeska.y:
                    print('\u2665 ', end='')
                else:
                    print('. ', end='')
            print()

    # premik heroja z inputi
    def input(self):
        global dx
        global dy
        self.stetjeKorakov += 1
        self.preostaliKoraki = self.maxKoraki - self.stetjeKorakov
        x, y = self.zemlja.hero.trenutna_pozicija()

        while True:
            uporabniskiInput = input('\033[92mVnesi dx med +2 in -2:\033[0m ')
            if uporabniskiInput == "q":
                sys.exit()
            try:
                dx = int(uporabniskiInput)
                if not (-2 <= dx <= 2):
                    print('\033[31mVnesli se številko izven razpona, ponovno vnesite številko dx.\033[0m')
                else:
                    break
            except ValueError:
                print('\033[31mProsim vnesite številko dx med +2 in -2.\033[0m')
        while True:
            uporabniskiInput = input('\033[92mVnesi dy med +2 in -2:\033[0m ')
            if uporabniskiInput == "q":
                sys.exit()
            try:
                dy = int(uporabniskiInput)
                if not (-2 <= dy <= 2):
                    print('\033[31mVnesli se številko izven razpona, ponovno vnesite številko dy.\033[0m')
                else:
                    break
            except ValueError:
                print('\033[31mProsim vnesite številko dy med +2 in -2.\033[0m')

        # če si izven omejitve zemlje se heroj izriše na drugi strani
        if x + dx > self.zemlja.sirina:
            self.zemlja.hero.x = x + dx - self.zemlja.sirina - 1
        elif x + dx < 0:
            self.zemlja.hero.x = x + dx + self.zemlja.sirina + 1
        elif y + dy > self.zemlja.visina:
            self.zemlja.hero.y = y + dy - self.zemlja.visina - 1
        elif y + dy < 0:
            self.zemlja.hero.y = y + dy + self.zemlja.visina + 1
        else:
            self.zemlja.hero.premikanje(dx=dx, dy=dy)

    def premakni_barabo(self):

        trenutnePozicijeBarab = []

        for b in self.zemlja.barabe:
            trenutnePozicijeBarab.append((b.x, b.y))

        for b in self.zemlja.barabe:
            trenutnePozicijeBarab.remove((b.x, b.y))
            b.nakljucno_gibanje()
            x, y = b.trenutna_pozicija()

            while (x, y) in trenutnePozicijeBarab:
                b.nakljucno_gibanje()
                x, y = b.trenutna_pozicija()
            trenutnePozicijeBarab.append((x, y))

    def end_game_loose(self):
        xh, yh = self.zemlja.hero.trenutna_pozicija()
        xp, yp = self.zemlja.princeska.trenutna_pozicija()

        for b in self.zemlja.barabe:
            xb, yb = b.trenutna_pozicija()
            # pogoji za konec igre
            if yh == yb and xb in range(xh - 1, xh + 2):
                print('\033[31mHeroj ujet!Konec igre...\033[0m')
                print(f'\033[92mVaš končni SCORE: {self.rezultat} in prišli ste do LEVEL: {self.level}\033[0m')
                return True
            elif xh == xb and yb in range(yh - 1, yh + 2):
                print('\033[31mHeroj ujet!Konec igre...\033[0m')
                print(f'\033[92mVaš končni SCORE: {self.rezultat} in prišli ste do LEVEL: {self.level}\033[0m')
                return True
            elif xb == xp and yb == yp:
                print('\033[31mBaraba ujela princesko!Konec igre...\033[0m')
                print(f'\033[92mVaš končni SCORE: {self.rezultat} in prišli ste do LEVEL: {self.level}\033[0m')
                return True
            elif self.stetjeKorakov == self.maxKoraki:
                print('\033[31mPresegli ste določeno število potez, igre konec!\033[0m')
                print(f'\033[92mVaš končni SCORE: {self.rezultat} in prišli ste do LEVEL: {self.level}\033[0m')

    def end_game_win(self):
        xh, yh = self.zemlja.hero.trenutna_pozicija()
        xp, yp = self.zemlja.princeska.trenutna_pozicija()

        if xh == xp and yh == yp:
            if self.level == 3:
                print(
                    f'\033[33mČestitke, končali ste igro, princesa in heroj živit srečno skupaj vse do konca svojih dni!\033[0m')
                print(f'\033[92mVaš končni SCORE: {self.rezultat} in prišli ste do LEVEL: {self.level}\033[0m')
                return True
            else:
                print('\033[32mPrinceska rešena...greš v naslednji nivo\033[0m')
                self.level += 1
                self.rezultat += (self.maxKoraki - self.stetjeKorakov) * 2
                return False

# prestavil importe po izvajanju kode zaradi errorja 'circular import', kjer se moduli kličejo v loopu...
from src.domain.baraba import Baraba
from src.domain.zemlja import Zemlja
from src.domain.hero import Hero
from src.domain.princeska import Princeska
