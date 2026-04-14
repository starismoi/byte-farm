import time
import pickle
import player_module
import farm_module
import trade_module
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
    player.quote = fn.quote_of_the_day()
    player.deity = fn.cursed_word(4,5).capitalize()
    return player

def save_game(player):
    with open("savefile.dat", "wb") as f:
        pickle.dump(player, f)

def continue_game():
    try:
        with open("savefile.dat", "rb") as f:
            return pickle.load(f)
    except:
        fn.error("No Save File Found!")
        return 1

def credits():
    fn.clear_screen()
    file = open("credits")
    print(file.read())
    quit = input("enter q to quit: ")
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
                if player == 1:
                    return
                return player
            elif choice == 3:
                credits()
            elif choice == 4:
                quit()

def save_and_return(player):
    save_game(player)
    menu()

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
            5 : lambda: save_and_return(player)
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
            return
    
    elif player.location == "Trade Center":
        print(f"1. View Market\n2. Sell Harvest\n3. Purchase\n4. Sacrifice\n5. Pray to {player.deity}\n6. Return\n")
        choice = input(": ")
        print("")
        func_dict = {
            1: lambda: trade_module.display_market(player),
            2: lambda: trade_module.display_market(player),
            3: lambda: trade_module.display_market(player),
            4: lambda: trade_module.display_market(player),
            5: lambda: trade_module.display_market(player),
            6: lambda: player_module.change_location(player, "Default"),
        }
        choice, type, validity = fn.checker_ultima(choice, len(func_dict))
        if validity:
            func_dict[choice]()
            return

    elif player.location == "Temple":
        pass

# Main

def time_cycle(player, hours):
    player.hour += hours
    daycount = 0
    if player.hour >= 24:
        while player.hour >= 24:
            player.hour -= 24
            farm_module.grow_plants(player)
            player.quote = fn.quote_of_the_day()
            daycount += 1
        player.day += daycount
    

def main():
    player = menu()
    fn.clear_screen()
    running = True
    last_time = time.time()
    while running:
        current_time = time.time()
        elapsed_time = current_time - last_time
        
        if elapsed_time > 1:
            time_cycle(player, elapsed_time)
            last_time = current_time
        fn.status_bar(player)
        actions(player)
        fn.clear_screen()
    
main()
