import fn
import item_module

class Player:
    def __init__(self, name="", farm = None, farm_name="", gold=100, location="Default", faith=1, inventory=None, day=0, hour=0):
        self.name = name
        self.farm = farm
        self.farm_name = farm_name
        self.gold = gold
        self.location = location
        self.faith = faith
        self.inventory = inventory
        self.day = day
        self.hour = hour
        self.quote = None
        self.deity = None

def open_inventory(player):
    inventory = player.inventory
    fn.clear_screen()
    fn.title("inventory")
    while True:
        for index, item in enumerate(inventory):
            if item.type == "Plant":
                print(f"{index}: {item.name} * {item.amount} (Rarity: {item.rarity} / Quality: {item.quality} / Mutation: {item.mutation})")
            else:
                print(f"{index}: {item.name} * {item.amount}")
        quit = input("\nenter q to exit: ")
        if quit == "q":
            break

def choose_item(player):
    inventory = player.inventory
    fn.clear_screen()
    fn.title("inventory")
    for index, item in enumerate(inventory):
        if item.type == "Plant":
            print(f"{index}: {item.name} * {item.amount} (Rarity: {item.rarity} / Quality: {item.quality} / Mutation: {item.mutation})")
        else:
            print(f"{index}: {item.name} * {item.amount}")
    try:
        index = int(input("\nselect an item: "))
        print("")
        item = inventory[index]
        return item
    except:
        print("That's not a valid index!\n")
        fn.wait()

def add_item(player, new_item):
    inventory = player.inventory
    if new_item.type in non_stackable_types:
        pass
    else:
        for item in inventory:
            if item.name == new_item.name:
                item.amount += new_item.amount
                return 0
    if len(inventory) + 1 <= inv_space:
        inventory.append(new_item)
        return 0
    else:
        return 1
    

def check_zero(player):
    inventory = player.inventory
    for item in inventory:
        if item.amount == 0:
            inventory.remove(item)

def change_location(player, destination):
    player.location = destination


locations = ["Default", "Farm", "Trade Center", "Temple"]
starting_inv = [item_module.Seed_Item("Radish Seed", "Radish", 3)]
inv_space = 20
non_stackable_types = ["Plant"]