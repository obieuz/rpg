class Shop:
    def __init__(self):
        self.items = []

    def buy(self,index,player_gold):
        if self.items[index] is None:
            return False
        if self.items[index].price > player_gold:
            return False
        return self.items.pop(index)
