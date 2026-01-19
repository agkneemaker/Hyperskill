import random
pencils = 0

while True:
    try:
        pencils = int(input("How many pencils?: "))
        if pencils < 0:
            pencils = int(input("The number of pencils must be numeric: "))
        elif pencils == 0:
            pencils = print("The number of pencils should be positive")
        else:
            break
    except ValueError:
        pencils = print("The number of pencils must be numeric")

pencils_num = pencils * "|"
name1, bot = "Agne", "Mo"
pick_user = input(f"Who will be the first player ({name1}, {bot}): ")

while pick_user != name1 and pick_user != bot:
    pick_user = input(f"Choose between {name1} and {bot}: ")

while pencils > 0:
    counter = 0
    if pick_user == name1:
        print("|" * pencils)
        counter = int(input(f"{name1}'s turn: "))
        while counter not in range(1,4):
            try:
                counter = int(input("Possible values: '1', '2' or '3': "))
            except ValueError:
                print("Please enter a numerical value between 1-3.")
        while counter > pencils:
            counter = int(input("Too many pencils were taken: "))
        pencils -= counter
        pick_user = bot

    elif pick_user == bot:
        print("|" * pencils)
        if pencils % 4 == 0 and pencils not in range(1,4):
            counter = 3
        elif pencils % 4 == 1 and pencils not in range(1,4):
            counter = random.randint(1,3)
        elif pencils % 4 == 2 and pencils not in range(1,4):
            counter = 1
        elif pencils % 4 == 3 and pencils not in range(1,4):
            counter = 2
        elif pencils == 2:
            counter = 1
        elif pencils == 3:
            counter = 2
        elif pencils == 1:
            counter = 1
        print(f"{bot}'s turn!")
        print(counter)
        pencils -= counter
        pick_user = name1

print(pick_user, "won!")