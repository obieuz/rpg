import pygame
from uuid import uuid4
from core.Items.Item import Item


class Shop:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Shop, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.items = []
            self.is_visible = False
            self.surface = pygame.Surface((1000, 1000))
            self.surface.fill((50, 50, 50))
            self.initialized = True

            self.initialize_items()

    def initialize_items(self):
        self.items.append(Item(
            id=uuid4(),
            _type="sword",
            _abilities={
                "strength":20,
            },
            _price=100,
            _icon="gui/miecz.png"
        ))

    def buy(self,uuid,player):
        item = next((x for x in self.items if x.id == uuid), None)
        if item is None:
            return False
        if item.price > player.gold:
            return False
        player.add_to_inventory(item)
        return self.items.remove(item)

    def toggle_is_visible(self):
        self.is_visible = not self.is_visible

    def draw(self, screen):
        if not self.is_visible:
            return False
        screen.blit(self.surface,(100,100))
        for item in self.items:
            item.draw_shop_item(screen)

    def handle_click(self, mouse_pos):
        if not self.is_visible:
            return None
        for item in self.items:
            if item.rect.collidepoint(mouse_pos):
                print(f"Clicked on item: {item.type}")
                return item
        return None


