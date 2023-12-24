import uuid
from khayyam import JalaliDatetime

class Item():
    Appetizer_list = list()
    Food_list = list()
    Beverage_list = list()

    def __init__(self, name, item_type, price):
        self.uuid = uuid.uuid4(),
        self.name = name,
        self.item_type = item_type,
        self.price = price,
        self.time = JalaliDatetime.now()
        if item_type.lower() == 'appetizer':
            Item.Appetizer_list.append(self)
        elif item_type.lower() == 'food':
            Item.Food_list.append(self)
        else:
            Item.Beverage_list.append(self)

    @classmethod
    def search(cls,name):
        items_list = list()
        items_list.extend(cls.Appetizer_list)
        items_list.extend(cls.Food_list)
        items_list.extend(cls.Beverage_list)
        for item in items_list:
            if item == name:
                return item
            return None

