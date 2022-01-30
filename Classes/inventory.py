class Item:
    def __init__(self,name,type,description,prop):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop
        self.amount = 0

    def start_amount(self):
        self.amount = 5

    def set_amount(self,i):
        self.amount = i

    def reduce_amount_by_one(self):
        self.amount -= 1

