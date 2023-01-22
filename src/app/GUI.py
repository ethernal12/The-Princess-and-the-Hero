from random import random, choice, randint

import pygame, sys
from pygame import font
from pygame.locals import *

from src.app._app import App
from src.app.config import GameConfig
from src.app.game_messages import messages
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
        # Set up pygame
        pygame.init()
        # Set up the window
        self.windowSurface = pygame.display.set_mode((width, height), 0, 32)

    def draw_game(self):
        # Fill the screen with a background color
        self.windowSurface.fill((255, 255, 255))
        # Draw a red rectangle on the screen
        dx = self.width / self.zemlja.sirina
        dy = self.height / self.zemlja.visina
        pygame.draw.rect(self.windowSurface, (25, 50, 0), (
            self.zemlja.hero.x * dx, self.zemlja.hero.y * dy, dx, dy))

        # Update the display
        pygame.display.update()

        stBarab = self.level * GameConfig.ST_BARAB.value
        self.maxKoraki = GameConfig.MAX_KORAKI.value

        # generiraj vse mozne kombinacije matrice
        for i in range(10):
            x = randint(0, self.width)
            y = randint(0, self.height)
            pygame.draw.rect(self.windowSurface, (255, 0, 0), (x, y, 20, 20))
        pygame.display.update()
        # Run the game loop
        # running = True
        # while running:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             running = False

        # Quit pygame
        # pygame.quit()

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
            x, y = choice(moznePozicije)

            barabe.append(Baraba(x=x, y=y, hitrost=GameConfig.HITROST_BARABE.value))
            # vsakic odstrani pozicijo barabe iz moznih pozicij
            moznePozicije.remove((x, y))
            pygame.display.update()
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
                    self.zemlja.premakni_heroja(-1, 0)
                elif event.key == pygame.K_d:
                    self.zemlja.premakni_heroja(1, 0)
                elif event.key == pygame.K_w:
                    self.zemlja.premakni_heroja(0, -1)
                elif event.key == pygame.K_s:
                    self.zemlja.premakni_heroja(0, 1)
                elif event.key == pygame.K_q:
                    sys.exit()

    def end_game_conditions(self):
        pass
    # Set up the colors
    # BLACK = (0, 0, 0)
    # RED = (255, 0, 0)
    # GREEN = (0, 255, 0)
    # BLUE = (0, 0, 255)
    # WHITE = (255, 255, 255)
    #
    # # Set up fonts
    # basicFont = pygame.font.SysFont(None, 48)
    #
    # # Set up the text
    # text = basicFont.render('HELLO WORLD', True, WHITE)
    # textRect = text.get_rect()
    # textRect.centerx = windowSurface.get_rect().centerx
    # textRect.centery = windowSurface.get_rect().centery
    #
    # # Draw the white background onto the surface
    # windowSurface.fill(WHITE)
    #
    # # Draw a blue poligon onto the surface
    # pygame.draw.polygon(windowSurface, BLUE, ((250, 0), (500, 200), (250, 400), (0, 200)))
    #
    # # Draw a green poligon onto the surface
    # pygame.draw.polygon(windowSurface, GREEN, ((125, 100), (375, 100), (375, 300), (125, 300)))
    #
    # # Draw a red circle onto the surface
    # pygame.draw.circle(windowSurface, RED, (250, 200), 125)
    #
    # # Get a pixel array of the surface
    # pixArray = pygame.PixelArray(windowSurface)
    # pixArray[480][380] = BLACK
    # del pixArray
    #
    # # Draw the text onto the surface
    # windowSurface.blit(text, textRect)
    #
    # # Draw the window onto the screen
    # pygame.display.update()
    #
    # # Run the game loop
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == QUIT:
    #             pygame.quit()
    #             sys.exit()


if __name__ == '__main__':
    app = GUI(300, 400)
    running = True
    app.new_game()
    while running:
        app.draw_game()
        app.input()
