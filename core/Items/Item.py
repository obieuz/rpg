import pygame
class Item:
    def __init__(self,id,_type,_price,_icon, _abilities):
        self.type = _type
        self.id = id
        self.abilities = _abilities
        self.price = _price
        self.icon = pygame.image.load(_icon).convert_alpha()
        self.rect = self.icon.get_rect()

    def draw_shop_item(self, screen, pos=(200, 200)):
        font = pygame.font.SysFont("Arial", 36)
        text_color = (255, 255, 255)
        self.rect = self.icon.get_rect(center=pos)
        screen.blit(self.icon, self.rect)
        text_surface = font.render(str(self.price), True, text_color)
        text_rect = text_surface.get_rect(center=(self.rect.centerx, self.rect.bottom + 20))
        screen.blit(text_surface, text_rect)

    def draw_overlay_item(self,screen,pos):
        self.rect = self.icon.get_rect(center=pos)
        screen.blit(self.icon, self.rect)

