import coffee_data

resources = coffee_data.resources
espresso = coffee_data.MENU["espresso"]
latte = coffee_data.MENU["latte"]
cappiccino = coffee_data.MENU["cappuccino"]

def handle_report():
    report = (f"Water: {resources['water']}\n"
    f"Milk: {resources['milk']}\n"
    f"Coffee: {resources['coffee']}")
    return report

# TODO check if resources are sufficient
def check_resources(choice):
    for ingredient in coffee_data.MENU[choice]["ingredients"]:
        amount_needed = coffee_data.MENU[choice]['ingredients'][ingredient]
        amount_left = coffee_data.resources[ingredient]
        if amount_needed > amount_left:
            print(f"Sorry we're all out {ingredient}")
        else:
            pass

# TODO Make the coffee
def handle_choice(choice):
    pass

# TODO process coins
def handle_payment():
    pass
    # TODO check if transaction is successful, if too much money, return change



machine_on = True

while machine_on:
    user_choice = input("What would you like to drink? (espresso/latte/cappuccino): \n").lower()

    # TODO Thank user for using coffemaker deluxe v10.0


    # TODO fix error with user_choice = off caused by check_resources
    if user_choice == "off":
        machine_on = False

    if user_choice == "report":
        print(handle_report())

    check_resources(user_choice)