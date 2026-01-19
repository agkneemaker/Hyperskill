pencils = 0

# how many pencils
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

# player names
pencils_num = pencils * "|"
name1, name2 = input("Please enter Player 1's name: "), input("Please enter Player 2's name: ")
pick_user = input(f"Who will be the first player ({name1}, {name2}): ")

while pick_user != name1 and pick_user != name2:
    pick_user = input(f"Choose between {name1} and {name2}: ")

# game itself
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
        pick_user = name2

    elif pick_user == name2:
        print("|" * pencils)
        counter = int(input(f"{name2}'s turn: "))
        while counter not in range(1,4):
            try:
                counter = int(input("Possible values: '1', '2' or '3': "))
            except ValueError:
                print("Please enter a numerical value between 1-3.")
        while counter > pencils:
            counter = int(input("Too many pencils were taken: "))
        pencils -= counter
        pick_user = name1

print(pick_user, "won!")
