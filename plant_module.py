class Plant:
    def __init__(self, species, rarity, stage, quality, mutation):
        self.species = species
        self.rarity = rarity
        self.stage = stage
        self.quality = quality
        self.mutation = mutation
        graphics = species+str(stage)
        self.graphics = graphics

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