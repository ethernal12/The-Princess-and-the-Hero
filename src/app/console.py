from dataclasses import dataclass
from src.domain.baraba import Baraba
from src.domain.zemlja import Zemlja
from src.domain.hero import Hero
from src.domain.princeska import Princeska
from src.app.config import GameConfig
from src.app.game_messages import messages
import random


@dataclass
class Console:
    zemlja: Zemlja = None
    level: int = GameConfig.LEVEL_INICIALIZACIJA.value
    maxKoraki: int = GameConfig.MAX_KORAKI.value
    rezultat: int = GameConfig.REZULTAT.value

    # end game con
    def end_game_conditions(self):
        xh, yh = self.zemlja.hero.x, self.zemlja.hero.y
        xp, yp = self.zemlja.princeska.x, self.zemlja.princeska.y

        if xh == xp and yh == yp:
            self.level += GameConfig.INKREMENT_LEVEL.value
            self.rezultat += self.maxKoraki * GameConfig.ST_BARAB.value
            if self.level > GameConfig.KONCNI_LEVEL.value:
                messages(self, GameConfig.ZMAGA)
                return GameConfig.ZMAGA
            else:
                messages(self, GameConfig.NASLEDNJI_NIVO)
                return GameConfig.NASLEDNJI_NIVO

        for b in self.zemlja.barabe:
            xb, yb = b.x, b.y
            if xb == xp and yb == yp:
                messages(self, GameConfig.PRINCESA_UJETA)
                return GameConfig.PRINCESA_UJETA
            elif yh == yb and xb in range(- GameConfig.ODDALJENOST_BARABE.value,
                                          GameConfig.ODDALJENOST_BARABE.value + 1):
                self.zemlja.hero.odtrani_zivljenje()
                messages(self, GameConfig.HEROJ_UJET)
                if len(self.zemlja.hero.st_ostalih_zivljenj()) == 0:
                    messages(self, GameConfig.PORAZ)
                    return GameConfig.HEROJ_UJET
                break
            elif xh == xb and yb in range(- GameConfig.ODDALJENOST_BARABE.value,
                                          GameConfig.ODDALJENOST_BARABE.value + 1):
                self.zemlja.hero.odtrani_zivljenje()
                messages(self, GameConfig.HEROJ_UJET)
                if len(self.zemlja.hero.st_ostalih_zivljenj()) == 0:
                    messages(self, GameConfig.PORAZ)
                    return GameConfig.HEROJ_UJET
                break
            elif self.maxKoraki == GameConfig.KORAKI_SPODNJA_MEJA.value:
                messages(self, GameConfig.KORAKI_PRESEZENI)
                return GameConfig.KORAKI_PRESEZENI
        return GameConfig.NADALJUJ_ZANKO

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
            barabe.append(Baraba(x=x, y=y, hitrost=GameConfig.HITROST_BARABE.value))
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
        messages(self, GameConfig.PODATKI_IGRE)
        messages(self, GameConfig.BORDER_TOP_BOTTOM)
        for y in range(self.zemlja.visina + 1):
            messages(self, GameConfig.BORDER_LEFT)
            for x in range(self.zemlja.sirina + 1):
                flag = False
                for b in self.zemlja.barabe:
                    if b.x == x and b.y == y:
                        messages(self, GameConfig.PRINT_BARABO)
                        flag = True
                        break
                if flag:
                    continue
                if x == self.zemlja.hero.x and y == self.zemlja.hero.y:
                    messages(self, GameConfig.PRINT_HEROJA)
                elif x == self.zemlja.princeska.x and y == self.zemlja.princeska.y:
                    messages(self, GameConfig.PRINT_PRINCESKE)
                else:
                    messages(self, GameConfig.NARISI_PIKO)
            messages(self, GameConfig.BORDER_RIGHT)
        messages(self, GameConfig.BORDER_TOP_BOTTOM)

    def input(self):

        input_koncan = False
        while not input_koncan:
            uporabniskiInput = messages(self, GameConfig.INPUT_SPOROCILO_DX)
            if uporabniskiInput == GameConfig.EXIT_GAME_INPUT.value:
                return GameConfig.EXIT_GAME_COMMAND
            try:
                dx = int(uporabniskiInput)
                if not dx in range(-GameConfig.HITROST_HEROJA.value, GameConfig.HITROST_HEROJA.value + 1):
                    messages(self, GameConfig.ERROR_INPUT_IZVEN_RAZPONE)
                else:
                    uporabniskiInput = messages(self, GameConfig.INPUT_SPOROCILO_DY)
                    if uporabniskiInput == GameConfig.EXIT_GAME_INPUT.value:
                        return GameConfig.EXIT_GAME_COMMAND
                    try:
                        dy = int(uporabniskiInput)
                        if not dy in range(-GameConfig.HITROST_HEROJA.value, GameConfig.HITROST_HEROJA.value + 1):
                            messages(self, GameConfig.ERROR_INPUT_IZVEN_RAZPONE)
                        else:
                            input_koncan = True
                    except ValueError:
                        messages(self, GameConfig.ERROR_INPUT_NI_STEVILKA)

            except ValueError:
                messages(self, GameConfig.ERROR_INPUT_NI_STEVILKA)
        self.maxKoraki -= GameConfig.KORAKI_DEKREMENT.value
        self.zemlja.premakni_heroja(dx, dy)
        return GameConfig.NADALJUJ_ZANKO
