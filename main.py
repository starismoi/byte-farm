import random
import math
import os
import sys

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

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
    def __init__(self, index, type, plant = "", soiled="", watered = ""):
        self.index = index
        self.type = type
        self.plant = plant
        self.soiled = soiled
        self.watered = watered
        if type == "Dirt" and soiled == True:
            soil_string = "Soiled"
            graphics = type+soil_string
        else:
            graphics = type
        self.graphics = graphics
    def soil(self):
        self.soiled = True
        self.graphics = self.type+"Soiled"

locations = ["Default", "Farm", "Trade Center", "Temple"]

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

# Tile initialization and weights
tile_types = ["Dirt", "Water", "Void"] # Or Plant
tile_types_p = [8.5,1.4,0.1]

# Farm things

farm = []
max_width = 10

tile_graphics = {
    "Dirt" : '#',
    "Water" : '~',
    "Void" : '0',
    "DirtSoiled" : '='
}

def generate(farm):
    for index in range(100):
        tile_choices = random.choices(tile_types, weights = tile_types_p)
        tile_type = random.choice(tile_choices)
        tile = Tile(index, tile_type)
        farm.append(tile)
    return farm

def render(farm, max_width):
    clear_screen()
    print("-------( f a r m )-------\n")
    rows = len(farm) // 10
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
        if tile % max_width == 0:
            print(f"\n{current_row}", end = "")
            current_row += 1
    print("\n")
    while True:
        quit = input("enter q to exit: ")
        print("")
        if quit == "q":
            break

def plant_seeds(farm):
    pass

def soil_dirt(farm):
    clear_screen()
    print("Select Dirt to Soil. (format: x, y)")
    x, y = input(": ").split(',')
    x, y = int(x), int(y)
    print("")
    index = x + (10 * y)
    tile = farm[index]
    if tile.type != "Dirt":
        print("This Tile is not Dirt.")
    elif tile.soiled == True:
        print("This Tile is already Soiled.")
    elif tile.plant != "":
        tile.plant = ""
    else:
        tile.soil()


# New Game / Continue logic (save files)

name = ""
farm_name = ""
gold = 100
location = ""
infamy = 1
inventory = [("Radish Seeds", 10)]
inv_size = 20

def open_inventory(inventory):
    clear_screen()
    while True:
        for item in inventory:
            print(item)
        quit = input("\nenter q to exit: ")
        if quit == "q":
            break

def start_game():
    global name, farm_name, location, farm

    while True:
        clear_screen()
        print("--------( b y t e f a r m )--------\n")
        print("1. New Game\n2. Continue\n3. Credits\n4. Quit\n")
        choice = int(input(": "))
        print("")
        if choice == 1:
            farm = generate(farm)
            location = "Default"
            clear_screen()
            name = input("What is your name?\n: ")
            farm_name = input("What is the name of your farm?\n: ")
            break
        elif choice == 2:
            break
        elif choice == 3:
            break
        elif choice == 4:
            quit()
        else:
            print(f"'{choice}' isn't an option.")

# Status Bar

def status_bar(name, farm_name, gold, location, infamy):
    print(f"{name} / {farm_name} Farm / {gold}G / @{location} / Infamy: {infamy}\n\n")

# Actions

def actions():
    global location

    print("-------( c h o i c e s )-------\n")
    if location == "Default":
        print("1. Visit Farm\n2. Visit Trade Center\n3. Visit Temple\n4. Open Inventory\n5. Return to Menu\n(returning to menu will save your progress!)\n")
        choice = int(input(": "))
        print("")
        if choice == 1:
            location = "Farm"
        elif choice == 2:
            location = "Trade Center"
        elif choice == 3:
            location = "Temple"
        elif choice == 4:
            open_inventory(inventory)
        elif choice == 5:
            start_game()

    elif location == "Farm":
        print("1. View Farm\n2. Plant Seeds\n3. Soil Dirt\n4. Harvest Crops\n5. Check Tile\n6. Return\n")
        choice = int(input(": "))
        print("")
        if choice == 1:
            render(farm, max_width)
        elif choice == 2:
            plant_seeds(farm)
        elif choice == 3:
            soil_dirt(farm)
        elif choice == 4:
            harvest_crops()
        elif choice == 5:
            check_tile()
        else:
            location = "Default"
        

def main():
    
    start_game()
    clear_screen()
    running = True
    while running:
        status_bar(name, farm_name, gold, location, infamy)
        actions()
        clear_screen()
    
main()