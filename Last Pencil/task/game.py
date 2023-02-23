import random

players = []


def bot(x):
    if x in range(4, 1000, 4):
        return 3
    elif x in range(3, 1000, 4):
        return 2
    elif x in range(2, 1000, 4):
        return 1
    elif (int(x) - 1) % 4 == 0:
        random.seed(x)
        return random.randint(1, 3)
    elif int(x) == 1:
        return 1
    elif int(x) == 0:
        return 0


def human(pencils):
    n = input()
    if n.isnumeric() is not True:
        print("Possible values: '1', '2' or '3'")
        return human(pencils)
    n = int(n)
    if int(n) != 1 and int(n) != 2 and int(n) != 3:
        print("Possible values: '1', '2' or '3'")
        return human(pencils)
    if int(n) > pencils:
        print("Too many pencils were taken")
        return human(pencils)
    else:
        return int(n)


def input_pencils():
    print("How many pencils would you like to use:")
    n = input()
    if n.isnumeric() is not True:
        print("The number of pencils should be numeric")
        return input_pencils()
    if int(n) == 0:
        print("The number of pencils should be positive")
        return input_pencils()
    else:
        return int(n)


def input_player():
    player = input()
    if player not in ["John", "Jack"]:
        print("Choose between 'John' and 'Jack'")
        return input_player()
    else:
        return player


def beginning():
    numbers_pencils = input_pencils()
    print("Who will be the first (John, Jack):")
    first_player = input_player()
    print("|" * numbers_pencils)
    return first_player, numbers_pencils


def main():
    first_player, numbers_pencils = beginning()
    current_name = first_player
    while numbers_pencils > 0:
        print(f"{current_name} turn!")
        if current_name == "John":
            numbers_pencils -= human(numbers_pencils)
        else:
            print(bot(numbers_pencils))
            numbers_pencils -= bot(numbers_pencils)
        print("|" * numbers_pencils)
        current_name = "Jack" if current_name == "John" else "John"
        if numbers_pencils <= 0:
            print(f"{current_name} won!")
            break


if __name__ == '__main__':
    main()

