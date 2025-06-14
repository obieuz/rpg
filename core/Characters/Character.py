import pygame.sprite

from core.Inventory import Inventory
from core.Timer import Timer
from ..Overlay import Overlay
from ..Shop import Shop
from ..settings import HITTING_TIMER_MS


class Character(pygame.sprite.Sprite):
    def __init__(self, pos, group, enemy_sprites, _color, _speed, _mana, _strength, _health):
        super().__init__(group)

        self.enemy_sprites = enemy_sprites
        self.image = pygame.Surface((32, 64))
        self.gold = 200

        self.image.fill(_color)
        self.rect = self.image.get_rect(center=pos)

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)

        self.speed = _speed

        self.inventory = Inventory()
        self.shop = Shop()
        self.overlay = Overlay()
        self.timers = {"hit" : Timer(200,self.hit)}

        self.hitting_range = 100

        self.range = 1
        self.mana = _mana
        self.strength = _strength
        self.health = _health
        self.shop_key_pressed = False

    def input(self):
        if not self.timers["hit"].active:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.direction.y = -1
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
            else:
                self.direction.y = 0

            if keys[pygame.K_LEFT]:
                self.direction.x = -1
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
            else:
                self.direction.x = 0

            if keys[pygame.K_s]:
                if not self.shop_key_pressed:
                    self.shop.toggle_is_visible()
                    self.shop_key_pressed = True
            else:
                self.shop_key_pressed = False

            if keys[pygame.K_k]:
                self.change_current_item(-1)

            if keys[pygame.K_l]:
                self.change_current_item(1)

            if keys[pygame.K_h]:
                self.timers["hit"].activate()
                self.direction = pygame.math.Vector2()

    def update(self, dt):
        self.input()
        self.move(dt)
        for timer in self.timers.values():
            timer.update()

    def move(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

    def add_to_inventory(self,item):
        self.inventory.add_item(item)

    def hit(self):
        print("chcesz kogos bic")
        for enemy in self.enemy_sprites:
            if not self.is_enemy_in_hitting_range(enemy):
                continue
            print("enemy uderzony")
            damage = self.strength
            enemy.dealt_damage(damage)


    def dealt_damage(self, damage):
        pass

    def is_enemy_in_hitting_range(self,enemy):
        #jak bedzie jakis item to brac range jego a nie postaci

        distance = self.pos.distance_to(enemy.pos)
        return distance <= self.hitting_range

    def change_current_item(self,value):
        self.inventory.change_active_item(value)


