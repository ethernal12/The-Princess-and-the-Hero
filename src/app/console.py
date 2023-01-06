from dataclasses import dataclass
from src.domain.baraba import Baraba
from src.domain.zemlja import Zemlja
from src.domain.hero import Hero
from src.domain.princeska import Princeska
from src.app.config import GameConfig

import random
from enum import Enum
from colored import fg, attr


class GameStates(Enum):
    HEROJ_UJET = "heroj_ujet"
    PRINCESA_UJETA = "princeska_ujeta"
    KORAKI_PRESEZENI = "koraki_preseženi"
    ZMAGA = "zmaga_končaj_igro"
    NASLEDNJI_NIVO = "naslednji_nivo"
    NADALJUJ_ZANKO = 'nadaljuj'


@dataclass
class Console:
    print(GameConfig.INKREMENT_LEVEL.value, 'value')
    zemlja: object = None
    level: int = GameConfig.INKREMENT_LEVEL.value
    maxKoraki: int = GameConfig.MAX_KORAKI.value
    rezultat: int = GameConfig.REZULTAT.value
    global result

    def end_game_conditions(self):
        xh, yh = self.zemlja.hero.x, self.zemlja.hero.y
        xp, yp = self.zemlja.princeska.x, self.zemlja.princeska.y

        if xh == xp and yh == yp:
            self.level += 1
            self.rezultat += self.maxKoraki * GameConfig.ST_BARAB.value
            if self.level > GameConfig.KONCNI_LEVEL.value:
                print(
                    f'{fg("gold_1")}Čestitke, končali ste igro, princesa in heroj živita srečno skupaj vse do konca '
                    f'svojih dni!')
                print(f'{fg("light_green")}Vaš končni SCORE: {self.rezultat} in prišli ste do LEVEL: {self.level}')
                return GameStates.ZMAGA
            else:
                print(f'{fg("light_green")}Princeska rešena...greš v naslednji nivo')
                return GameStates.NASLEDNJI_NIVO

        for b in self.zemlja.barabe:
            xb, yb = b.x, b.y

            if yh == yb and xb in range(xh - 1, xh + 2):
                self.zemlja.hero.odtrani_zivljenje()
                print(f'{fg("red_1")}Heroj ujet! Število življenj = {self.zemlja.hero.st_ostalih_zivljenj()}{attr(0)}')
                if len(self.zemlja.hero.st_ostalih_zivljenj()) == 0:
                    print(f'{fg("red_1")}Konec igre... {attr(0)}')
                    print(
                        f'{fg("light_green")}Vaš končni SCORE: {self.rezultat} in prišli ste do LEVEL: {self.level}{attr(0)}')
                    return GameStates.HEROJ_UJET
                break
            elif xh == xb and yb in range(yh - 1, yh + 2):
                self.zemlja.hero.odtrani_zivljenje()
                print(f'{fg("red_1")}Heroj ujet! Število življenj = {self.zemlja.hero.st_ostalih_zivljenj()}{attr(0)}')
                if len(self.zemlja.hero.st_ostalih_zivljenj()) == 0:
                    print(f'{fg("red_1")}Konec igre... {attr(0)}')

                    print(
                        f'{fg("light_green")}Vaš končni SCORE: {self.rezultat} in prišli ste do LEVEL: {self.level}{attr(0)}')
                    return GameStates.HEROJ_UJET
                break
            elif xb == xp and yb == yp:
                print(f'{fg("red_1")}Baraba ujela princesko!Konec igre... {attr(0)}')
                print(
                    f'{fg("light_green")}Vaš končni SCORE: {self.rezultat} in prišli ste do LEVEL: {self.level}{attr(0)}')
                return GameStates.PRINCESA_UJETA

            elif self.maxKoraki == 0:
                print(f'{fg("red_1")}Presegli ste določeno število potez, igre konec! {attr(0)}')
                print(
                    f'{fg("light_green")}Vaš končni SCORE: {self.rezultat} in prišli ste do LEVEL: {self.level}{attr(0)}')
                return GameStates.KORAKI_PRESEZENI
        return GameStates.NADALJUJ_ZANKO

    def new_game(self):
        barabe: list[Baraba] = []
        stBarab = self.level * GameConfig.ST_BARAB.value
        sirina = GameConfig.SIRINA_ZEMLJE.value - self.level
        visina = GameConfig.VISINA_ZEMLJE.value - self.level
        self.maxKoraki = GameConfig.MAX_KORAKI.value
        # generiraj vse mozne kombinacije matrice
        moznePozicije = [(x, y) for x in range(sirina) for y in range(visina)]
        for i in range(stBarab):
            # izberi med pozicijami, ki so še na voljo
            x, y = random.choice(moznePozicije)
            barabe.append(Baraba(x=x, y=y, hitrost=GameConfig.HITROST_BARABE.value, visina=visina, sirina=sirina))
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
                y=yh,
            ),
            princeska=Princeska(
                x=xp,
                y=yp),
            barabe=barabe,
            dx=0,
            dy=0
        )

    def draw_game(self):
        print(f'{self.zemlja.hero.st_ostalih_zivljenj()}')
        #
        print(f'{fg("gold_1")}{self.level} LEVEL{attr(0)}')
        print(f'{fg("gold_1")}SCORE {self.rezultat}{attr(0)}')
        print('---------')
        print(f'{fg("gold_1")}Preostali koraki {self.maxKoraki}{attr(0)}')
        print('-------------------')
        for y in range(self.zemlja.visina + 1):
            for x in range(self.zemlja.sirina + 1):
                flag = False
                for b in self.zemlja.barabe:
                    if b.x == x and b.y == y:
                        print(fg('red_1') + 'B ' + attr('reset'), end='')
                        flag = True
                        break
                if flag:
                    continue
                if x == self.zemlja.hero.x and y == self.zemlja.hero.y:
                    print(fg('light_green') + 'H ' + attr('reset'), end='')
                elif x == self.zemlja.princeska.x and y == self.zemlja.princeska.y:
                    print('\u2640 ', end='')
                else:
                    print('. ', end='')
            print()

        # premik heroja z inputi

    def input(self):
        self.maxKoraki -= 1

        input_koncan = False
        while not input_koncan:
            uporabniskiInput = input(fg('light_green') + 'Vnesi dx med +2 in -2:' + attr('reset'))
            if uporabniskiInput == GameConfig.EXIT_GAME_INPUT.value:
                return GameConfig.EXIT_GAME_COMMAND
            try:
                dx = int(uporabniskiInput)
                if not dx in range(-GameConfig.HITROST_HEROJA.value, GameConfig.HITROST_HEROJA.value + 1):
                    print(
                        fg('red_1') + 'Vnesli se številko izven razpona, ponovno vnesite številko dx.' + attr('reset'))
                else:
                    uporabniskiInput = input(fg('light_green') + 'Vnesi dy med +2 in -2:' + attr('reset'))
                    if uporabniskiInput == GameConfig.EXIT_GAME_INPUT.value:
                        return GameConfig.EXIT_GAME_COMMAND
                    try:
                        dy = int(uporabniskiInput)
                        if not dy in range(-GameConfig.HITROST_HEROJA.value, GameConfig.HITROST_HEROJA.value + 1):
                            print(fg('red') + 'Vnesli se številko izven razpona, ponovno vnesite številko dy.' + attr(
                                'reset'))
                        else:
                            input_koncan = True
                    except ValueError:
                        print(fg('red_1') + 'Prosim vnesite številko dy med +2 in -2' + attr(
                            'reset'))
            except ValueError:
                print(fg('red_1') + 'Prosim vnesite številko dx med +2 in -2' + attr(
                    'reset'))

        self.zemlja.premakni_heroja(dx, dy)
        return GameStates.NADALJUJ_ZANKO
