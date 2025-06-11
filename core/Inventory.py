class Inventory:
    def __init__(self):
        self.slots = 10
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
        return True

    def wear_armor(self,item):
        if item.type not in self.armor.keys():
            return False

