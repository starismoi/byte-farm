import random
import os
import time

class Player:
    def __init__(self, name="", farm = [], farm_name="", gold=100, location="Default", faith=1, inventory=[]):
        self.name = name
        self.farm = farm
        self.farm_name = farm_name
        self.gold = gold
        self.location = location
        self.faith = faith
        self.inventory = inventory

class Plant:
    def __init__(self, species, rarity, stage, quality, mutation):
        self.species = species
        self.rarity = rarity
        self.stage = stage
        self.quality = quality
        self.mutation = mutation
        graphics = species+stage
        self.graphic = graphics
    
class Tile:
    def __init__(self, index, type, plant = "None", soiled=False):
        self.index = index
        self.type = type
        self.plant = plant
        self.soiled = soiled
        if type == "Dirt" and soiled == True:
            soil_string = "Soiled"
            graphics = type+soil_string
        else:
            graphics = type
        self.graphics = graphics
    def soil(self):
        self.soiled = True
        self.graphics = self.type+"Soiled"

class Item:
    def __init__(self, name, amount, type):
        self.name = name
        self.amount = amount
        self.type = type

class Seed_Item(Item):
    def __init__(self, name, species, amount, type="Seed"):
        self.name = name
        self.species = species
        self.amount = amount
        self.type = type

class Plant_Item(Plant, Item):
    def __init__(self, plant_obj, amount, type="Plant"):
        self.__dict__.update(plant_obj.__dict__)
        self.name = self.species
        self.amount = amount
        self.type = type

locations = ["Default", "Farm", "Trade Center", "Temple"]

# Functionality

def open_inventory(player):
    inventory = player.inventory
    clear_screen()
    title("inventory")
    while True:
        for item in inventory:
            print(item)
        quit = input("\nenter q to exit: ")
        if quit == "q":
            break

def choose_item(player):
    inventory = player.inventory
    clear_screen()
    title("inventory")
    i = 0
    for item in inventory:
        print(i, item)
        i += 1
    try:
        index = int(input("\nselect an item: "))
        item = inventory[index]
        return item
    except:
        print("That's not a valid index!\n")
        wait()

def wait():
    time.sleep(1.5)

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def title(word):
    charlist = list(word)
    formatted = ""
    for char in charlist:
        formatted = formatted + " " + char
    formatted += " "
    print(f"-----------({formatted})----------\n")

def get_index():
    value = input("Enter coordinates (: x, y) or index (: i)\n: ")
    try:
        x, y = value.split(",")
        try:
            x, y = int(x), int(y)
            index = x + (10 * y)
            return index
        except:
            ("These are not valid coordinates!")
            wait()
    except:
        try:
            index = int(value)
            return index
        except:
            print("This is not a valid index!")
            wait()

# Plant things

species = ["Radish", "Dandelion", "Raspberries"]
species_graphics = {
    "Radish0" : ".",
    "Radish1" : ",",
    "Radish2" : "v",
    "Radish3" : "V",
    "Dandelion0" : ".",
    "Dandelion1" : ",",
    "Dandelion2" : "o",
    "Dandelion3" : "*",
    "Raspberries0" : ".",
    "Raspberries1" : ",",
    "Raspberries2" : "@",
    "Raspberries3" : "r",
}
species_rarity = {
    "Radish" : 1,
    "Dandelion" : 1,
    "Raspberries" : 2
}

mutations = ["None", "Dreamscape", "Nightmare", "Enlightened", "Treacherous"]
mutations_p = [100,5,5,1,1]

# Tile initialization and weights
tile_types = ["Dirt", "Water", "Void"] # Or Plant
tile_types_p = [50,5,0.5]

# Farm things

farm = []
max_width = 10

tile_graphics = {
    "Dirt" : '#',
    "Water" : '~',
    "Void" : '0',
    "DirtSoiled" : '='
}

def generate():
    farm = []
    for index in range(100):
        tile_choices = random.choices(tile_types, weights = tile_types_p)
        tile_type = random.choice(tile_choices)
        tile = Tile(index, tile_type)
        farm.append(tile)
    return farm

def render(player):
    farm = player.farm
    max_width = 10
    clear_screen()
    title("farm")
    current_row = 0
    print(" ", end = "") # left indentation
    for x in range(max_width):
        print(x, end = "") # column numbers
    print("")
    tile = 0
    print(current_row, end = "")
    current_row += 1
    while tile < len(farm):
        if farm[tile].type == "Plant":
            print(species_graphics[farm[tile].plant.graphics])
        else:
            print(tile_graphics[farm[tile].graphics], end = "")
        tile += 1
        if tile % max_width == 0 and current_row < (len(farm) / max_width):
            print(f"\n{current_row}", end = "")
            current_row += 1
    print("\n")
    while True:
        quit = input("enter q to exit: ")
        print("")
        if quit == "q":
            break

def plant_seeds(player):
    clear_screen()
    title("planting")
    farm = player.farm
    soiled_tiles = []
    for tile in farm:
        if tile.soiled == True:
            soiled_tiles.append(tile)
    if len(soiled_tiles) == 0:
        print("There are no Soiled Dirt Tiles!\n")
        wait()
    else:
        print("Select a Seed to plant from your Inventory.")
        try:
            seed = choose_item(player)
            if seed.type != "Seed":
                print("This item is not a seed.")
                wait()
                return
        except:
            return
        print("Where would you like to plant this seed?")
        index = get_index()
        tile = farm[index]
        if tile in soiled_tiles:
            species = seed.plant
            quality = random.rand()
            rarity = species_rarity[species]
            mutation_choices = random.choices(mutations, mutations_p)
            mutation = random.choice(mutation_choices)
            plant = Plant(species, rarity, 0, quality, mutation)
            tile.plant = plant
        else:
            print("This tile is not a valid tile.")
            wait()
                
def soil_dirt(player):
    clear_screen()
    title("soiling")
    print("Where would you like to soil?")
    index = get_index()
    tile = player.farm[index]
    if tile.type != "Dirt":
        print("This Tile is not Dirt.")
        wait()
    elif tile.soiled == True:
        print("This Tile is already Soiled.")
        wait()
    elif tile.plant != "None":
        tile.plant = "None"
    else:
        tile.soil()

def harvest_crops(player):
    title("harvest crops")
    pass

def check_tile(player):
    clear_screen()
    farm = player.farm
    title("check tile")
    index = get_index()
    try:
        tile = farm[index]
        print("Type:", tile.type)
        print("Plant:", tile.plant)
        print("Soiled:", tile.soiled, "\n")
        quit = input("enter q to quit: ")
        print("")
        if quit == "q":
            return
    except:
        print("This is not a valid tile.")
        wait()
        return
        
# New Game / Continue logic (save files)

def start_game():

    while True:
        clear_screen()
        title("bytefarm")
        print("1. New Game\n2. Continue\n3. Credits\n4. Quit\n")
        choice = int(input(": "))
        print("")
        if choice == 1:
            farm = generate()
            location = "Default"
            clear_screen()
            name = input("What is your name?\n: ")
            farm_name = input("What is the name of your farm?\n: ")
            gold = 100
            faith = 1
            inventory = []
            player = Player(name, farm, farm_name, gold, location, faith, inventory)
            return player
        elif choice == 2:
            break
        elif choice == 3:
            break
        elif choice == 4:
            quit()
        else:
            print(f"'{choice}' isn't an option.")
            wait()

# Status Bar

def status_bar(player):
    name = player.name
    farm_name = player.farm_name
    gold = player.gold
    location = player.location
    faith = player.faith
    print(f"{name} / {farm_name} Farm / {gold}G / @{location} / Faith: {faith}\n\n")

# Actions

def actions(player):

    title("actions")
    if player.location == "Default":
        print("1. Visit Farm\n2. Visit Trade Center\n3. Visit Temple\n4. Open Inventory\n5. Return to Menu\n(returning to menu will save your progress!)\n")
        choice = int(input(": "))
        print("")
        if choice == 1:
            player.location = "Farm"
        elif choice == 2:
            player.location = "Trade Center"
        elif choice == 3:
            player.location = "Temple"
        elif choice == 4:
            open_inventory(player)
        elif choice == 5:
            start_game()
        else:
            print(f"{choice} isn't an option.")
            wait()

    elif player.location == "Farm":
        print("1. View Farm\n2. Plant Seeds\n3. Soil Dirt\n4. Harvest Crops\n5. Check Tile\n6. Open Inventory\n7. Return")
        choice = int(input(": "))
        print("")
        if choice == 1:
            render(player)
        elif choice == 2:
            plant_seeds(player)
        elif choice == 3:
            soil_dirt(player)
        elif choice == 4:
            harvest_crops(player)
        elif choice == 5:
            check_tile(player)
        elif choice == 6:
            open_inventory(player)
        elif choice == 7:
            player.location = "Default"
        else:
            print(f"{choice} isn't an option.")
            wait()
    
    elif player.location == "Trade Center":
        pass
        
def main():
    
    player = start_game()
    clear_screen()
    running = True
    while running:
        status_bar(player)
        actions(player)
        clear_screen()
    
main()