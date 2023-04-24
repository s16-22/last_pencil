# Write your code here

import math

water = 400
milk = 540
beans = 120
disposable_cups = 9
money = 550
price_espresso = 4
price_latte = 7
price_cappuccino = 6
norm_espresso = [250, 0, 16]
norm_latte = [350, 75, 20]
norm_cappuccino = [200, 100, 12]
norm = []
reserves = [water, milk, beans]


def consumption_espresso():
    global water, beans, disposable_cups, money
    result = []
    for i in range(0, 3, 2):
        result.append(math.floor(reserves[i]/norm_espresso[i]))
    if reserves[0] < 250:
        print("Sorry, not enough water!")
        print()
    elif reserves[2] < 16:
        print("Sorry, not enough coffee beans!")
        print()
    elif min(result) >= 1:
        print("I have enough resources, making you a coffee!")
        print()
        water -= 250
        beans -= 16
        disposable_cups -= 1
        money += price_espresso
        reserves[0] = water
        reserves[1] = milk
        reserves[2] = beans
    return water, beans, disposable_cups, money, reserves


def consumption_latte():
    global water, milk, beans, disposable_cups, money
    result = []
    for i in range(len(reserves)):
        result.append(math.floor(reserves[i]/norm_latte[i]))
    if reserves[0] < 350:
        print("Sorry, not enough water!")
        print()
    elif reserves[1] < 75:
        print("Sorry, not enough milk!")
        print()
    elif reserves[2] < 20:
        print("Sorry, not enough coffee beans!")
        print()
    elif min(result) >= 1:
        print("I have enough resources, making you a coffee!")
        print()
        water -= 350
        milk -= 75
        beans -= 20
        disposable_cups -= 1
        money += price_latte
        reserves[0] = water
        reserves[1] = milk
        reserves[2] = beans
    return water, milk, beans, disposable_cups, money, reserves


def consumption_cappuccino():
    global water, milk, beans, disposable_cups, money
    result = []
    for i in range(len(reserves)):
        result.append(math.floor(reserves[i]/norm_cappuccino[i]))
    if reserves[0] < 200:
        print("Sorry, not enough water!")
        print()
    elif reserves[1] < 100:
        print("Sorry, not enough milk!")
        print()
    elif reserves[2] < 12:
        print("Sorry, not enough coffee beans!")
        print()
    elif min(result) >= 1:
        print("I have enough resources, making you a coffee!")
        print()
        water -= 200
        milk -= 100
        beans -= 12
        disposable_cups -= 1
        money += price_cappuccino
        reserves[0] = water
        reserves[1] = milk
        reserves[2] = beans
    return water, milk, beans, disposable_cups, money, reserves


def print_reserves():
    global water, milk, beans, disposable_cups, money
    print(f"""
The coffee machine has:
{water} ml of water
{milk} ml of milk
{beans} g of coffee beans
{disposable_cups} disposable cups
${money} of money
    """)


def buy():
    global water, milk, beans, disposable_cups, money
    print()
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    kind_coffee = input()
    if kind_coffee == "1":
        consumption_espresso()
    elif kind_coffee == "2":
        consumption_latte()
    elif kind_coffee == "3":
        consumption_cappuccino()
    return water, milk, beans, disposable_cups


def fill():
    global water, milk, beans, disposable_cups
    print()
    print("Write how many ml of water you want to add: ")
    _water = input()
    print("Write how many ml of milk you want to add: ")
    _milk = input()
    print("Write how many grams of coffee beans you want to add:")
    _beans = input()
    print("Write how many disposable cups you want to add:")
    _disposable_cups = input()
    water += int(_water)
    milk += int(_milk)
    beans += int(_beans)
    disposable_cups += int(_disposable_cups)
    reserves[0] = water
    reserves[1] = milk
    reserves[2] = beans
    print()
    return water, milk, beans, disposable_cups, reserves


def main():
    global money
    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == 'buy':
            buy()
        elif action == 'fill':
            fill()
        elif action == 'take':
            print()
            print(f"I gave you ${money}")
            print()
            money -= money
        elif action == 'remaining':
            print_reserves()
        elif action == 'exit':
            break


if __name__ == '__main__':
    main()



# print("Write how many ml of water the coffee machine has:")
# water = int(input())
# print("Write how many ml of milk the coffee machine has:")
# milk = int(input())
# print("Write how many grams of coffee beans the coffee machine has:")
# coffee = int(input())
# print("Write how many cups of coffee you will need:")
# cups = int(input())
# norm = [200, 50, 15]
# n = [water, milk, coffee]
# result = []
#
# for i in range(len(norm)):
#     result.append(math.floor(n[i]/norm[i]))
# if min(result) == cups:
#     print("Yes, I can make that amount of coffee")
# elif min(result) < cups:
#     print(f"No, I can make only {min(result)} cups of coffee")
# elif min(result) > cups:
#     print(f"Yes, I can make that amount of coffee (and even {abs(cups-min(result))} more than that)")
