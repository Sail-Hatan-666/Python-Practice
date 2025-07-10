from coffee_data import MENU
from coffee_data import resources
from coffee_data import profit


def handle_report():
    report = (f"Water: {resources['water']}\n"
    f"Milk: {resources['milk']}\n"
    f"Coffee: {resources['coffee']}")
    return report


def check_resources(choice):
    missing_ingredients = []
    for ingredient in MENU[choice]["ingredients"]:
        amount_needed = MENU[choice]['ingredients'][ingredient]
        amount_left = resources[ingredient]
        if amount_needed > amount_left:
            missing_ingredients.append(ingredient)
    if len(missing_ingredients) == 0:
        return True
    else: 
        return False


# TODO Make the coffee
def make_coffee(choice):
    for key in MENU[choice]["ingredients"]:
        if key in resources:
            updated_value = resources[key] - MENU["ingredients"][key]
            resources[key] = updated_value


# TODO process coins
def handle_payment(
        choice, 
        quarters, 
        dimes, 
        nickels, 
        pennies
        ):
    cost = MENU[choice]["cost"]
    total = quarters + dimes + nickels + pennies
    total_format = f"${quarters + dimes + nickels + pennies:.2f}"
    change = f"{total - cost:.2f}"
    if total < cost:
        change = None
        return False, total_format, change
    elif total > cost:
         return True, total_format, change
    elif total == cost:
        return True, total_format, change


machine_on = True

while machine_on:

    user_choice = input(
        "What would you like to drink? "
        "(espresso $1.50/latte $2.50/cappuccino $3.00): \n"
        ).lower()
    
    pennies = int(input("How many pennies?")) * 0.01
    dimes = int(input("How many dimes?")) * 0.05
    nickles = int(input("How many nickles?")) * 0.1
    quarters = int(input("How many quarters?")) * 0.25

    if user_choice == "off":
        machine_on = False
    
    if user_choice == "report":
        print(handle_report())

    if user_choice in MENU:
        if not check_resources(user_choice):
            pass
    else:
        print("Please enter a valid option.")


    # TODO add function to refill the machine perhaps this, off and report can \
    # only be handled by an admin with a password?