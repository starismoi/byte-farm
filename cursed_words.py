import random
import sys

if len(sys.argv) not in [4,5] and not ("--help" in sys.argv or "-h" in sys.argv):
    print("Usage: <filename> cycles min_tokens max_tokens (type) (--help or -h for help)")
    quit()

if "--help" in sys.argv or "-h" in sys.argv:
    print("Python cursed word generator! (1.0)")
    print("cycles - Result Count\nmin_tokens - Minimum Tokens of Word\nmax_tokens - Maximum Tokens of Word\ntype - town, city, forest, name")
    quit()

cycles = int(sys.argv[1])
min_tokens = int(sys.argv[2])
max_tokens = int(sys.argv[3])
try:
    result_type = sys.argv[4]
except IndexError:
    result_type = "default"

vowels = ["a","i","e","o","u","ae","ie","ei","ö","ü","ee"]
vowels_p = []
for vowel in vowels:
    if vowel in ["ae","ie"]:
        vowels_p.append(4.7)
    elif vowel in ["ü","ö"]:
        vowels_p.append(4.3)
    elif vowel == "ee":
        vowels_p.append(4)
    else:
        vowels_p.append(5)
consonants = ["b","f","j","k","l","m","n","p","q","r","s","v","x","y"]
cons_con = ["c","d","g","w","z","t"]
cons_sfx = ["h","t","sch"]
cons_sfx_p = [5,5,4.5]
s_sfx = ["h","t"]

def first_token():
    set_choice = random.choice([vowels,consonants,cons_sfx])
    token_choice = random.choice(set_choice)
    return token_choice

def choose_token(set):
    if set == cons_sfx:
        set = random.choices(set, weights = cons_sfx_p)
    elif set == vowels:
        set = random.choices(set, weights = vowels_p)
    choice = random.choice(set)
    return choice

def return_token(token, prev_token, old_token):
    if token in vowels:
        set_choice = random.choice([consonants, cons_sfx, cons_con])
        token_choice = choose_token(set_choice)
        return token_choice
    elif token in ["l", "r"]:
        if prev_token in vowels:
            set_choice = random.choice([vowels, consonants, cons_con, cons_sfx])
        else:
            set_choice = vowels
        token_choice = choose_token(set_choice)
        return token_choice
    elif token == "s":
        set_choice = random.choice([vowels, s_sfx])
        token_choice = choose_token(set_choice)
        return token_choice
    elif token in cons_con:
        set_choice = random.choice([vowels, cons_sfx])
        token_choice = choose_token(set_choice)
        if prev_token == "t" and old_token == "t":
            token_choice = choose_token(vowels)
        return token_choice
    else:
        token_choice = choose_token(vowels)
        return token_choice

def word_gen():
    if min_tokens == max_tokens:
        length = min_tokens
    else:
        length = random.randint(min_tokens, max_tokens)
    word = ""
    token = first_token()
    prev_token = ""
    old_token = ""
    word = word + token
    for t in range(length):
        old_token = prev_token
        prev_token = token
        token = return_token(token, prev_token, old_token)
        word = word + token
    return word

for i in range(cycles):
    if result_type == "town":
        word = word_gen()
        word = word.title()
        print(word, "town")
    elif result_type == "city":
        word = word_gen()
        word = word.title()
        choice = random.choice(["city", "burg"])
        if choice == "city":
            print(word, "city")
        elif choice == "burg":
            print(word+"burg")
    elif result_type == "forest":
        word = word_gen()
        word = word.title()
        choice = random.choice(["forest","woods"])
        if choice == "forest":
            print(word, "forest")
        elif choice == "woods":
            print(word, "woods")
    elif result_type == "name":
        first = word_gen()
        first = first.title()
        last = word_gen()
        last=last.title()
        print(first, last)
    elif result_type == "default":
        word = word_gen()
        print(word)

