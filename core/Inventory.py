class Inventory:
    def __init__(self):
        self.slots = 10
        self.items = []

    def add_item(self,item):
        if len(self.items) > self.slots:
            return False
        self.items.append(item)
        return True
