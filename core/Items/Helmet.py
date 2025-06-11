from core.Items.Item import Item


class Helmet(Item):
    def __init__(self,_price,_icon,_abilities):
        super().__init__("helmet",_price,_icon,_abilities)
