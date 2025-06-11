import pygame

from core.Characters.Character import Character
from core.Characters.Warrior import Warrior
from core.Enemies.Enemy import Enemy


class Level:
    def __init__(self):
        self.player = None
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        self.player = Warrior((640,320),self.all_sprites,self.enemy_sprites)

        Enemy(1,(800,320),self.enemy_sprites)

    def run(self,dt):
        self.display_surface.fill("black")
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)

        self.enemy_sprites.draw(self.display_surface)
        self.enemy_sprites.update(dt,self.player)