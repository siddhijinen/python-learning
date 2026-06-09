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

def check_resources(ordered_drink, avl_resources):
    missing = []
    recipe = MENU[ordered_drink]["ingredients"]
    for item in recipe:
        if recipe[item] > avl_resources[item]:
            missing.append(item)
    return missing

def process_money():
    print("Please insert coins.")
    try:
        q = int(input("How many quarters?: ") or 0)
        d = int(input("How many dimes?: ") or 0)
        n = int(input("How many nickels?: ") or 0)
        p = int(input("How many pennies?: ") or 0)
    except ValueError:
        print("Invalid input. Assuming 0 for that coin.")
        return 0
    return q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01

def make_coffee(drink, rsrc):
    recipe = MENU[drink]["ingredients"]
    for item in recipe:
        rsrc[item] -= recipe[item]

def main():
    profit = 0
    use_machine = True
    while use_machine:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit:.2f}\n")
            continue
        elif user_input == "off":
            print("Machine turned off.")
            use_machine = False
            break
        if user_input not in MENU:
            print("Invalid choice. Please select espresso, latte, or cappuccino.")
            continue
        missing_ingredients = check_resources(user_input, resources)
        if missing_ingredients:
            print(f"Sorry there is not enough {', '.join(missing_ingredients)}")
            continue
        else:
            money_to_receive = MENU[user_input]["cost"]
            print(f"That will be {money_to_receive}.")
        paid = process_money()
        if not paid >= money_to_receive:
            print("Sorry that's not enough money. Money refunded.")
            continue
        else:
            profit += money_to_receive
            if paid > money_to_receive:
                print(f"Here is ${paid-money_to_receive:.2f} in change.")
            make_coffee(user_input, resources)
            print(f"Here is your {user_input}. Enjoy!\n")

if __name__ == "__main__":
    start = input("Would you like to turn on the machine? (y/n): ").lower()
    if start == 'y':
        main()
    else:
        print("Program Ended.")
