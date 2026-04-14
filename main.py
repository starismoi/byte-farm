import player_module
import farm_module
import fn
        
# New Game / Continue logic (save files)

def new_game():
    fn.clear_screen()
    farm = farm_module.generate()
    name = input("What is your name?\n\n: ")
    print("")
    farm_name = input("What is the name of your farm?\n\n: ")
    print("")
    player = player_module.Player(name, farm, farm_name, 100, "Default", 1, player_module.starting_inv)
    return player

def continue_game():
    pass

def credits():
    fn.clear_screen()
    file = open("credits")
    print(file.read())
    quit = input("\nenter q to quit: ")
    if quit == "q":
        file.close()
        return

def menu():
    while True:
        fn.clear_screen()
        fn.title("bytefarm")
        print("1. New Game\n2. Continue\n3. Credits\n4. Quit\n")
        choice = input(": ")
        choice, type, validity = fn.checker_ultima(choice, 4)
        print("")
        if validity:
            if choice == 1:
                player = new_game()
                return player
            elif choice == 2:
                player = continue_game()
                return player
            elif choice == 3:
                credits()
            elif choice == 4:
                quit()

# Actions

def actions(player):
    fn.title("actions")
    if player.location == "Default":
        print("1. Visit Farm\n2. Visit Trade Center\n3. Visit Temple\n4. Open Inventory\n5. Return to Menu\n(returning to menu will save your progress!)\n")
        choice = input(": ")
        print("")
        func_dict = {
            1 : lambda: player_module.change_location(player, "Farm"),
            2 : lambda: player_module.change_location(player, "Trade Center"),
            3 : lambda: player_module.change_location(player, "Temple"),
            4 : lambda: player_module.open_inventory(player),
            5 : menu
        }
        choice, type, validity =  fn.checker_ultima(choice, len(func_dict))
        if validity:
            func_dict[choice]()

    elif player.location == "Farm":
        print("1. View Farm\n2. Plant Seeds\n3. Soil Dirt\n4. Harvest Crops\n5. Check Tile\n6. Open Inventory\n7. Return\n")
        choice = input(": ")
        print("")
        func_dict = {
            1 : lambda: farm_module.render(player),
            2 : lambda: farm_module.plant_seeds(player),
            3 : lambda: farm_module.soil_dirt(player),
            4 : lambda: farm_module.harvest_crops(player),
            5 : lambda: farm_module.check_tile(player),
            6 : lambda: player_module.open_inventory(player),
            7 : lambda: player_module.change_location(player, "Default")
        }
        choice, type, validity =  fn.checker_ultima(choice, len(func_dict))
        if validity:
            func_dict[choice]()
    
    elif player.location == "Trade Center":
        pass

    elif player.location == "Temple":
        pass

# Main

def main():
    player = menu()
    fn.clear_screen()
    running = True
    while running:
        fn.status_bar(player)
        actions(player)
        fn.clear_screen()
    
main()