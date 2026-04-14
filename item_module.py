import plant_module

class Item:
    def __init__(self,  name, amount, type):
        self.name = name
        self.amount = amount
        self.type = type

class Seed_Item(Item):
    def __init__(self, name, species, amount, type="Seed"):
        self.name = name
        self.species = species
        self.amount = amount
        self.type = type

class Plant_Item(plant_module.Plant, Item):
    def __init__(self, plant_obj, amount, type="Plant"):
        self.__dict__.update(plant_obj.__dict__)
        self.name = self.species
        self.amount = amount
        self.type = type