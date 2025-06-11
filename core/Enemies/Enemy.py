from core.Timer import Timer
from core.settings import ENEMY_BASE_HP, ENEMY_BASE_STRENGTH, ENEMY_BASE_STAMINA, ENEMY_BASE_VISION_RANGE, \
    ENEMY_BASE_SPEED, BASE_HITTING_RANGE, HITTING_TIMER_MS
import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, _level,pos, group):
        super().__init__(group)
        self.level = _level

        self.image = pygame.Surface((32, 32))
        self.image.fill("red")
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()
        self.active_item = None

        self.health = ENEMY_BASE_HP * _level
        self.strength = ENEMY_BASE_STRENGTH * _level
        self.stamina = ENEMY_BASE_STAMINA * _level

        self.vision_range = ENEMY_BASE_VISION_RANGE * _level
        self.speed = ENEMY_BASE_SPEED * _level
        self.hitting_range = BASE_HITTING_RANGE

    def update(self,dt,player):
        if self.is_player_in_vision_range(player):
            self.move(dt,player.pos)
        if self.is_player_in_hit_range(player):
            self.hit(player)

    def move(self,dt,player_pos):
        if player_pos.x > self.pos.x:
            self.direction.x = 1
        elif player_pos.x < self.pos.x:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if player_pos.y > self.pos.y:
            self.direction.y = 1
        elif player_pos.y < self.pos.y:
            self.direction.y = -1
        else:
            self.direction.y = 0

        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

    def is_player_in_vision_range(self,player):
        distance = self.pos.distance_to(player.pos)
        return distance <= self.vision_range

    def is_player_in_hit_range(self,player):
        distance = self.pos.distance_to(player.pos)
        return distance <= self.hitting_range

    def hit(self,player):
        damage = self.strength
        player.dealt_damage(damage)

    def dealt_damage(self,damage):
        print("Przeciwnik został uderzony")



