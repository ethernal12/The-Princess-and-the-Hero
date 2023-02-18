from random import random, choice, randint

import pygame, sys

from src.app._app import App
from src.app.GUIgameMessages import messages
from src.domain.baraba import Baraba
from src.domain.hero import Hero
from src.domain.princeska import Princeska
from src.domain.zemlja import Zemlja
from src.app.config import GameConfig


class GUI(App):
    def __init__(self, width, height):
        self.zemlja = None
        self.width = width
        self.height = height
        self.level = 1
        self.velikostFigur = 15
        # Set up pygame
        pygame.init()
        # Set up the window
        self.windowSurface = pygame.display.set_mode((width, height), 0, 32)
        self.rezultat: int = GameConfig.REZULTAT.value

    def draw_game(self):
        # Fill the screen with a background color
        self.windowSurface.fill((255, 255, 255))

        dx = self.width / self.zemlja.sirina
        dy = self.height / self.zemlja.visina
        # nariši grid ( self.zemlja.sirina * self.zemlja.visina)
        # ------------------
        # vertikalna linija
        for i in range(self.zemlja.sirina):
            # koordinate  x,y (0, 80), (400, 80)
            pygame.draw.line(self.windowSurface, (0, 0, 0), (i * (self.width / self.zemlja.sirina), 0),
                             (i * (self.width / self.zemlja.sirina), self.height))
        # horizontalna linija
        for i in range(self.zemlja.visina):
            pygame.draw.line(self.windowSurface, (0, 0, 0), (0, i * (self.height / self.zemlja.visina)),
                             (self.width, i * self.height / self.zemlja.visina))
        # -----------------
        # nariši princesko
        pygame.draw.rect(self.windowSurface, (238, 130, 238), (
            self.zemlja.princeska.x * dx + 8, self.zemlja.princeska.y * dy + 8,
            (self.width / self.zemlja.visina) - self.velikostFigur,
            (self.height / self.zemlja.sirina) - self.velikostFigur))
        # nariši heroja
        pygame.draw.rect(self.windowSurface, (25, 50, 0), (
            self.zemlja.hero.x * dx + 8, self.zemlja.hero.y * dy + 8,
            self.width / self.zemlja.visina - self.velikostFigur,
            self.height / self.zemlja.sirina - self.velikostFigur))
        # nariši barabo
        for b in self.zemlja.barabe:
            pygame.draw.rect(self.windowSurface, (255, 0, 0),
                             (b.x * dx + 8, b.y * dy + 8, (self.width / self.zemlja.visina - self.velikostFigur),
                              (self.height / self.zemlja.sirina) - self.velikostFigur))
            pygame.display.update()

    def new_game(self):
        barabe: list[Baraba] = []
        stBarab = self.level * GameConfig.ST_BARAB.value
        sirina = GameConfig.SIRINA_ZEMLJE.value - self.level
        visina = GameConfig.VISINA_ZEMLJE.value - self.level
        self.maxKoraki = GameConfig.MAX_KORAKI.value

        # generiraj vse mozne kombinacije matrice
        moznePozicije = [(x, y) for x in range(sirina) for y in range(visina)]
        self.badguys = []
        for i in range(stBarab):
            x, y = choice(moznePozicije)
            moznePozicije.remove((x, y))
            barabe.append(Baraba(x=x, y=y, hitrost=GameConfig.HITROST_BARABE.value))

        # izberi pozicije za heroja in princesko
        xh, yh = choice(moznePozicije)
        moznePozicije.remove((xh, yh))
        xp, yp = choice(moznePozicije)
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

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pygame.display.update()
                    self.zemlja.premakni_heroja(-1, 0)
                elif event.key == pygame.K_d:
                    self.zemlja.premakni_heroja(1, 0)
                elif event.key == pygame.K_w:
                    self.zemlja.premakni_heroja(0, -1)
                elif event.key == pygame.K_s:
                    self.zemlja.premakni_heroja(0, 1)
                elif event.key == pygame.K_q:
                    sys.exit()
                self.zemlja.premakni_barabo()

    def end_game_conditions(self):
        xh, yh = self.zemlja.hero.x, self.zemlja.hero.y
        xp, yp = self.zemlja.princeska.x, self.zemlja.princeska.y
        if xh == xp and yh == yp:

            self.level += GameConfig.INKREMENT_LEVEL.value
            self.rezultat += self.maxKoraki * GameConfig.ST_BARAB.value
            if self.level > GameConfig.KONCNI_LEVEL.value:
                messages(self.windowSurface, GameConfig.ZMAGA)
                return GameConfig.ZMAGA
            else:
                messages(self.windowSurface, GameConfig.NASLEDNJI_NIVO)
                return GameConfig.NASLEDNJI_NIVO

        for b in self.zemlja.barabe:
            xb, yb = b.x, b.y
            if xb == xp and yb == yp:
                messages(self.windowSurface, GameConfig.PRINCESA_UJETA)
                return GameConfig.PRINCESA_UJETA
            # elif yh == yb and xb in range(- GameConfig.ODDALJENOST_BARABE.value,
            #                               GameConfig.ODDALJENOST_BARABE.value + 1):
            #     self.zemlja.hero.odtrani_zivljenje()
            #     messages(self.windowSurface, GameConfig.HEROJ_UJET)
            #     if len(self.zemlja.hero.st_ostalih_zivljenj()) == 0:
            #         messages(self.windowSurface, GameConfig.PORAZ)
            #         return GameConfig.HEROJ_UJET
            #     break
            elif self.maxKoraki == GameConfig.KORAKI_SPODNJA_MEJA.value:
                messages(self.windowSurface, GameConfig.KORAKI_PRESEZENI)
                return GameConfig.KORAKI_PRESEZENI
        return GameConfig.NADALJUJ_ZANKO


if __name__ == '__main__':
    app = GUI(500, 400)
    running = True
    app.new_game()
    while running:
        result = app.end_game_conditions()
        app.draw_game()
        app.input()
        match result.value:
            case GameConfig.HEROJ_UJET.value:
                break
            case GameConfig.PRINCESA_UJETA.value:
                break
            case GameConfig.ZMAGA.value:
                break
            case GameConfig.KORAKI_PRESEZENI.value:
                break
            case GameConfig.NASLEDNJI_NIVO.value:
                app.new_game()
            case GameConfig.NADALJUJ_ZANKO.value:
                continue
        pygame.display.update()
