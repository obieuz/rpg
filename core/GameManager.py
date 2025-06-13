import pygame.display
from core.Overlay import Overlay

from core.Shop import Shop
from settings import *
from Level import Level
import sys


class GameManager:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("RPG")
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.shop = Shop()
        self.overlay = Overlay()

    def run(self):
        pygame.init()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    clicked_item = self.shop.handle_click(mouse_pos)
                    if clicked_item:
                        self.shop.buy(clicked_item.id,self.level.player)

            dt = self.clock.tick() / 1000
            self.level.run(dt)
            self.shop.draw(self.screen)
            self.overlay.draw(self.screen,self.level.player)
            pygame.display.update()


if __name__ == '__main__':
    game = GameManager()
    game.run()
