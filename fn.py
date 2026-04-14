import time
import os
import subprocess
import random

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
            if not type(x) == int or not type(y) == int:
                error("These are not valid coordinates!")
                return "Invalid"
            index = x + (10 * y)
            return index
        except:
            error("These are not valid coordinates!")
    except:
        try:
            index = int(value)
            if type(index) != int:
                error("This is not a valid index!")
                return "Invalid"
            return index
        except:
            error("This is not a valid index!")
    return "Invalid"

def status_bar(player):
    name = player.name
    farm_name = player.farm_name
    gold = player.gold
    location = player.location
    faith = player.faith
    day = player.day
    hour = player.hour
    if hour > 12:
        hour_display, sfx = hour - 12, "PM"
    else:
        hour_display, sfx = hour, "AM"
    print(f"{name} / {farm_name} / {gold}G / @{location} / Faith: {faith} / Day: {int(day)} / {int(hour_display)} {sfx}\n")

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

def error(msg):
    print(msg)
    wait()

# cursed words usage

def cursed_word(min, max):
    result = subprocess.run(
        ["python3", "cursed_words.py", "1", str(min), str(max)], 
        capture_output=True, 
        text=True
    )
    result = result.stdout.strip()
    return result

def quote_of_the_day():
    quote = ""
    quote_length = random.randint(4,5)
    for i in range(quote_length):
        word = cursed_word(2, 4)
        quote = quote + word + " "
    return quote

