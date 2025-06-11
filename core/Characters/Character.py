import pygame.sprite

from core.Inventory import Inventory
from core.Timer import Timer
from ..settings import HITTING_TIMER_MS


class Character(pygame.sprite.Sprite):
    def __init__(self, pos, group, enemy_sprites, _color, _speed, _mana, _strength, _health):
        super().__init__(group)

        self.enemy_sprites = enemy_sprites
        self.image = pygame.Surface((32, 64))
        self.gold = 0

        self.image.fill(_color)
        self.rect = self.image.get_rect(center=pos)

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)

        self.speed = _speed

        self.inventory = Inventory()

        self.hitting_range = 100

        self.range = 1
        self.mana = _mana
        self.strength = _strength
        self.health = _health

    def input(self):
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

        if keys[pygame.K_h]:
            #dodac timer
            self.hit()

    def update(self, dt):
        self.input()
        self.move(dt)

    def move(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

    def hit(self):
        print("chcesz kogos bic")
        for enemy in self.enemy_sprites:
            if not self.is_enemy_in_hitting_range(enemy):
                continue
            print("enemy uderzony")
            damage = self.strength
            enemy.dealt_damage(damage)


    def dealt_damage(self, damage):
        print(f"Player dostał {damage}")
        pass

    def is_enemy_in_hitting_range(self,enemy):
        #jak bedzie jakis item to brac range jego a nie postaci

        distance = self.pos.distance_to(enemy.pos)
        print(distance)
        return distance <= self.hitting_range


