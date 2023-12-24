import uuid
from khayyam import JalaliDatetime
from menu import Item

class order():
    def __init__(self, item_dict, in_out, table_number):
        self.uuid = uuid.uuid4()
        self.item_dict = item_dict
        self.in_out = in_out
        self.time = JalaliDatetime.now()


    def assign_table(self, table_number):
        pass

    def create_bill(self):
        return self.total_price 
    
    @property
    def total_price(self):
        item_names_list = [key for key in self.item_dict]
        total_price = 0
        for order in item_names_list:
            item_price = Item.search(order).price
            total_price += self.item_dict[order] * item_price
        return total_price
