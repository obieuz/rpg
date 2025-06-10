
characters_types = {
    "1":{
        "hp":100,
        "strength":20,
        "mana":0,
        "magical_power":0
    },
    "2":{
        "hp":80,
        "strength":5,
        "mana":20,
        "magical_power":20
    }
}

class Character:
    def __init__(self,character_type):
        self.character_type = character_type

        abilities = characters_types[character_type]

        self.hp = abilities["hp"]
        self.strength = abilities["strength"]
        self.mana = abilities["mana"]
        self.magical_power = abilities["magical_power"]



