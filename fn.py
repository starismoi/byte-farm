import time
import os

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
    value = input("\nEnter coordinates (: x, y) or index (: i)\n\n: ")
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
    return "Invalid"

def status_bar(player):
    name = player.name
    farm_name = player.farm_name
    gold = player.gold
    location = player.location
    faith = player.faith
    print(f"{name} / {farm_name} / {gold}G / @{location} / Faith: {faith}\n")

def option_check(type, action, condition):
    if type == int:
        try:
            action = int(action)
            if action <= condition:
                return True
            else:
                action_error(action)
        except:
            action_error(action)
    elif type == str:
        if action == condition:
            return True
        else:
            action_error(action)

def checker_ultima(action, condition):
    try:
        action = int(action)
        type = int
    except:
        type = str

    if type == int:
        return int(action), type, option_check(type, action, condition) # eg. True, int / False, int.
    else:
        return action, type, option_check(type, action, condition)
    
def action_error(action):
    print(f"{action} isn't an action!")
    wait()

def tile_error(tile):
    print(f"{tile} isn't a valid tile!")
    wait()