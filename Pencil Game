pencils = 0
while pencils <= 0:
    try:
        pencils = int(input("How many pencils?: "))
        if pencils < 0:
            pencils = int(input("The number of pencils must be numeric: "))
    except ValueError:
        pencils = int(input(("The number of pencils must be numeric: ")))
        if pencils == 0:
            pencils = int(input("The number of pencils should be positive: "))

pencils_num = pencils * "|"
name1, name2 = str(input("Player 1's Name: ")), str(input("Player 2's Name: "))
pick_user = input(f"Who will be the first player ({name1}, {name2}): ")

while pick_user != name1 and pick_user != name2:
    pick_user = input(f"Choose between {name1} and {name2}: ")

while pencils > 0:
    counter = 0
    if pick_user == name1:
        print("|" * pencils)
        counter = int(input(f"{name1}'s turn: "))
        while counter not in range(1,4):
            counter = int(input("Possible values: '1', '2' or '3': "))
        while counter > pencils:
            counter = int(input("Too many pencils were taken: "))
        pencils -= counter
        pick_user = name2

    elif pick_user == name2:
        print("|" * pencils)
        counter = int(input(f"{name2}'s turn: "))
        while counter not in range(1,4):
            counter = int(input("Possible values: '1', '2' or '3': "))
        while counter > pencils:
            counter = int(input("Too many pencils were taken: "))
        pencils -= counter
        pick_user = name1

print(pick_user, "won!")
