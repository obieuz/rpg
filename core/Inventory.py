import pygame


class Inventory:
    def __init__(self):
        self.slots = 3
        self.active_item_index = 0
        self.active_item = None
        self.items = []
        self.armor = {
            "helmet": None,
            "chestplate": None,
            "leggings": None,
            "boots": None
        }

    def add_item(self,item):
        if len(self.items) > self.slots:
            return False
        self.items.append(item)
        self.active_item = item
        self.active_item_index = self.items.index(self.active_item)
        return True

    def wear_armor(self,item):
        if item.type not in self.armor.keys():
            return False
        self.armor[item.type] = item

    def get_active_item(self):
        if len(self.items) == 0:
            return None
        return self.items[self.active_item_index]

    def change_active_item(self,value):
        self.active_item_index += value
        if self.active_item_index > len(self.items)-1:
            self.active_item_index = 0
        elif self.active_item_index < 0:
            self.active_item_index = len(self.items)-1

        self.active_item = self.items[self.active_item_index]

    def draw(self,screen):
        current_height = pygame.display.get_surface().get_height()
        for index,item in enumerate(self.items):
            item.draw(screen,(index*20,current_height-30))


