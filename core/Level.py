import pygame

from core.Characters.Character import Character
from core.Characters.Warrior import Warrior
from core.Enemies.Enemy import Enemy


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.level = 1
        self.enemies = 3

        self.setup()

    def setup(self):
        for i in range(self.enemies):
            Enemy(self.level,(800 - i*20,320),self.enemy_sprites)

    def run(self,dt,player):
        self.display_surface.fill("black")
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)

        self.enemy_sprites.draw(self.display_surface)
        self.enemy_sprites.update(dt,player)