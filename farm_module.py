import random
import fn
import player_module
import plant_module

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

    def harvest(self, plant_type):
        harvest = self.plant
        self.plant = "None"
        return harvest

# Tile initialization and weights
tile_types = ["Dirt", "Water", "Void"]
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
    fn.clear_screen()
    fn.title("farm")
    current_row = 0
    print(" ", end = "") # left indentation
    for x in range(max_width):
        print(x, end = "") # column numbers
    print("")
    tile = 0
    print(current_row, end = "")
    current_row += 1
    while tile < len(farm):
        if farm[tile].plant != "None":
            print(plant_module.species_graphics[farm[tile].plant.graphics], end = "")
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
    fn.clear_screen()
    fn.title("planting")
    farm = player.farm
    soiled_tiles = []
    for tile in farm:
        if tile.soiled == True:
            soiled_tiles.append(tile)
    if len(soiled_tiles) == 0:
        print("There are no Soiled Dirt Tiles!\n")
        fn.wait()
    else:
        print("Select a Seed to plant from your Inventory.")
        try:
            seed = player_module.choose_item(player)
            if seed.type != "Seed":
                print("This item is not a seed.")
                fn.wait()
                return
        except:
            return
        print("\nWhere would you like to plant this seed?\n")
        index = fn.get_index()
        tile = farm[index]
        if tile in soiled_tiles:
            species = seed.species
            quality = random.randint(1, 100) / 100
            rarity = plant_module.species_rarity[species]
            mutation_choices = random.choices(plant_module.mutations, plant_module.mutations_p)
            mutation = random.choice(mutation_choices)
            plant = plant_module.Plant(species, rarity, 0, quality, mutation)
            tile.plant = plant
            seed.amount -= 1
        else:
            print("This tile is not a valid tile.")
            fn.wait()
                
def soil_dirt(player):
    fn.clear_screen()
    fn.title("soiling")
    print("Where would you like to soil?")
    index = fn.get_index()
    tile = player.farm[index]
    if tile.type != "Dirt":
        print("This Tile is not Dirt.")
        fn.wait()
    elif tile.soiled == True:
        print("This Tile is already Soiled.")
        fn.wait()
    elif tile.plant != "None":
        tile.plant = "None"
    else:
        tile.soil()

def harvest_crops(player):
    fn.title("harvest crops")
    pass

def check_tile(player):
    fn.clear_screen()
    farm = player.farm
    fn.title("check tile")
    index = fn.get_index()
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
        fn.wait()
        return