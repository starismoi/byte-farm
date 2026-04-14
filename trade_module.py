import fn
import random

class Harvest:
    def __init__(self, name):
        self.name = name
        self.price = None
        self.last_price = None
        self.inertia_vector = None

def set_initial_price(harvest):
    for harvest in harvests:
        price = random.randint(20,30)
        harvest.price = price
        last_price = random.randint(20,30)
        harvest.last_price = last_price

def update_price(harvest, inertia_vector):
    price = harvest.price

def display_market(player):
    while True:
        fn.clear_screen()
        fn.title("the market")
        print(f"< Quote of the day: {player.quote}>\n")
        fn.title("stocks")
        fn.title("purchase")
        quit = input("enter q to quit: ")
        if quit == "q":
            break

harvests = [Harvest("Radish"), Harvest("Dandelion"), Harvest("Raspberries")]