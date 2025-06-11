from core.Characters.Character import Character


class Warrior(Character):
    def __init__(self,pos,group):
        super().__init__(pos,group,"yellow",250,20,10,30,20)
