#tworze overlay, tu jest hp, sila itp, inventory tu sie rysouje i sigma
import pygame
from pygame import Surface


class Overlay:
    def __init__(self):
        self.initialized = True
    def draw(self,screen,player):
        self.draw_inventory(screen,player.inventory)

    def draw_inventory(self,screen,inventory):
        current_width = pygame.display.get_surface().get_width()
        current_height = pygame.display.get_surface().get_height()

        for enum,item in enumerate(inventory.items):
            if enum == inventory.active_item_index:
                background = Surface((item.icon.get_width()-2,item.icon.get_height()-2))
                background.fill((0,255,0))
                screen.blit(background,(2+current_width//2 + enum*item.icon.get_width(),2+current_height-item.icon.get_height()))
            screen.blit(item.icon,(current_width//2 + enum*item.icon.get_width(),current_height-item.icon.get_height()))


