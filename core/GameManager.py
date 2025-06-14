import pygame.display

from core.Characters.Warrior import Warrior
from core.Overlay import Overlay
from core.Saver import Saver

from core.Shop import Shop
from settings import *
from Level import Level
import sys
import pickle


class GameManager:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("RPG")
        self.clock = pygame.time.Clock()
        self.shop = Shop()
        self.overlay = Overlay()
        self.player = None
        self.saver = Saver(self.player)

        self.level = Level()
        self.levels = [Level()]
        self.setup()


    def setup(self):
        self.player = Warrior((640, 320), self.level.all_sprites, self.level.enemy_sprites)

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
                        self.shop.buy(clicked_item.id,self.player)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    elif event.key == pygame.K_o:
                        self.saver.save()
                    elif event.key == pygame.K_p:
                        player = self.saver.load(1)
                        if player is not None:
                            self.player = player
            dt = self.clock.tick() / 1000
            self.level.run(dt,self.player)
            self.shop.draw(self.screen)
            self.overlay.draw(self.screen,self.player)
            pygame.display.update()


if __name__ == '__main__':
    game = GameManager()
    game.run()
