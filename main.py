MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

import art
print(art.logo)

def check_supply(ingredients):
    for i in ingredients:
        if ingredients[i] >= resources[i]:
            print(f"Sorry there is not enough {i} .")
            return False
    return True


def coin_process():
    print("Please insert coins.")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickles?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total

    
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']} ml ")
        print(f"Milk: {resources['milk']} ml ")
        print(f"Coffee: {resources['coffee']} ml ")
        print(f"Money: ${profit}")
    else:
        if check_supply(MENU[choice]["ingredients"]):
            payment = coin_process()
            if payment >= MENU[choice]["cost"]:
                changes = round(payment - MENU[choice]["cost"], 2)
                print(f"Here is ${changes} in change.")
                print("Here is your cappuccino ☕️. Enjoy!")
                profit += MENU[choice]["cost"]

                for item in MENU[choice]["ingredients"]:
                    resources[item] -= MENU[choice]["ingredients"][item]
                # print(f"Here is your {MENU[choice]} ☕️. Enjoy!")

            else:
                print("Sorry that's not enough money. Money refunded.")