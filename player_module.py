import fn
import item_module

class Player:
    def __init__(self, name="", farm = [], farm_name="", gold=100, location="Default", faith=1, inventory=[], day=0, hour=0):
        self.name = name
        self.farm = farm
        self.farm_name = farm_name
        self.gold = gold
        self.location = location
        self.faith = faith
        self.inventory = inventory
        self.day = day
        self.hour = hour

def open_inventory(player):
    inventory = player.inventory
    fn.clear_screen()
    fn.title("inventory")
    while True:
        for index, item in enumerate(inventory):
            print(f"{index}: {item.name} * {item.amount}")
        quit = input("\nenter q to exit: ")
        if quit == "q":
            break

def choose_item(player):
    inventory = player.inventory
    fn.clear_screen()
    fn.title("inventory")
    for index, item in enumerate(inventory):
        print(f"{index}: {item.name} * {item.amount}")
    try:
        index = int(input("\nselect an item: "))
        item = inventory[index]
        return item
    except:
        print("That's not a valid index!\n")
        fn.wait()

def add_item(player, new_item):
    inventory = player.inventory
    for item in inventory:
        if new_item.name == item.name:
            item.amount += new_item.amount
            return
        else:
            if len(inventory) + 1 < inv_space:
                inventory.append(new_item)
                return
            else:
                fn.error("Your inventory is full!")
                return "Invalid"

def check_zero(player):
    inventory = player.inventory
    for item in inventory:
        if item.amount == 0:
            inventory.remove(item.name)

def change_location(player, destination):
    player.location = destination


locations = ["Default", "Farm", "Trade Center", "Temple"]
starting_inv = [item_module.Seed_Item("Radish Seed", "Radish", 10)]
inv_space = 20