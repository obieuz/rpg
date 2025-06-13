#tworze overlay, tu jest hp, sila itp, inventory tu sie rysouje i sigma
import pygame


class Overlay:
    def __init__(self):
        self.initialized = True
    def draw(self,screen,player):
        self.draw_inventory(screen,player.inventory)

    def draw_inventory(self,screen,inventory):
        current_width = pygame.display.get_surface().get_width()
        current_height = pygame.display.get_surface().get_height()

        for enum,item in enumerate(inventory.items):
            screen.blit(item.icon,(current_width//2 + enum*item.icon.get_width(),current_height-item.icon.get_height()))


