from core.Characters.Character import Character


class Warrior(Character):
    def __init__(self,pos,group,enemy_sprites):
        super().__init__(pos,group,enemy_sprites,"yellow",250,20,10,20)
