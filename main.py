MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money_in_machine = 0


def print_report():
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: € {money_in_machine}€")


def check_resources(coffee_ingredients):
    for ingredient in coffee_ingredients:
        if coffee_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    else:
        return True


def brew_coffee(coffee_type, ordered_coffee_ingredients):
    for ingredient in ordered_coffee_ingredients:
        resources[ingredient] -= ordered_coffee_ingredients[ingredient]
    print(f"Here is your {coffee_type} ☕️. Enjoy!")


def handle_coins():
    print("Please insert coins")
    amount = int(input("How many quarters?: ")) * 0.25
    amount += int(input("How many dimes?: ")) * 0.1
    amount += int(input("How many nickles?: ")) * 0.05
    amount += int(input("How many cents?: ")) * 0.01
    return amount


def is_enough_paid(paid_sum, coffee_price):
    balance = round(paid_sum - coffee_price,2)
    if balance >= 0:
        print(f"Here is {balance} € in change.")
        global money_in_machine
        money_in_machine += coffee_price
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


machine_is_on = True

while machine_is_on:
    order = input("What would you like? (espresso/latte/cappuccino):").lower()
    if order == "report":
        print_report()
    elif order == "off":
        machine_is_on = False
    else:
        ordered_coffee = MENU[order]
        if check_resources(ordered_coffee['ingredients']):
            money_paid = handle_coins()
            if is_enough_paid(money_paid, ordered_coffee['cost']):
                brew_coffee(order, ordered_coffee['ingredients'])



# TODO: DONE 1. print report of resources
# TODO: DONE 2. check that there are sufficient resources
# TODO: DONE 3. off - turn machine off, end program
# TODO: DONE 4. make selected coffee deducting resources
# TODO: DONE 5. coin handling
# TODO: DONE 6. check there is enough money and process transaction


