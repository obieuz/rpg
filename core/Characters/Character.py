import pygame.sprite

from core.Inventory import Inventory


class Character(pygame.sprite.Sprite):
    def __init__(self, pos, group, _color,_speed,_stamina,_mana,_strength,_health):
        super().__init__(group)

        self.image = pygame.Surface((32, 64))
        self.gold = 0

        self.image.fill(_color)
        self.rect = self.image.get_rect(center=pos)

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)

        self.speed = _speed
        self.armor = {
            "helmet":None,
            "chestplate":None,
            "leggings":None,
            "boots":None
        }

        self.inventory = Inventory()

        self.range = 1
        self.stamina = _stamina
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

        print(self.direction)

    def update(self, dt):
        self.input()
        self.move(dt)

    def move(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

    def hit(self):
        pass
