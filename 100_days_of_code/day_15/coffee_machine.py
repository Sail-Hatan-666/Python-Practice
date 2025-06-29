import coffee_data

resources = coffee_data.resources
MENU = coffee_data.MENU


def handle_report():
    report = (f"Water: {resources['water']}\n"
    f"Milk: {resources['milk']}\n"
    f"Coffee: {resources['coffee']}")
    return report


def check_resources(choice):
    missing_ingredients = []
    for ingredient in coffee_data.MENU[choice]["ingredients"]:
        amount_needed = coffee_data.MENU[choice]['ingredients'][ingredient]
        amount_left = coffee_data.resources[ingredient]
        if amount_needed > amount_left:
            missing_ingredients.append(ingredient)
    return missing_ingredients


# TODO Make the coffee
def make_coffee(choice):
    for key in MENU[choice]["ingredients"]:
        if key in resources:
            updated_value = resources[key] - MENU[choice]["ingredients"][key]
            resources[key] = updated_value
    return f"Your {choice} is ready! Enjoy carefully as products are hot!"


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
    if total < cost:
        return (f"Your total is {total_format}. Sorry that's not enough money."
                "Transaction cancelled.")
    elif total >= cost:
        if total == cost:
            return f"Your total is {total_format}. {make_coffee (choice)}."
        elif total > cost:
            return (f"Your total is {total_format}. {make_coffee (choice)}."
                    f"Heres is ${total - cost:.2f} in change.")


machine_on = True

while machine_on:

    user_choice = input(
        "What would you like to drink? "
        "(espresso $1.50/latte $2.50/cappuccino $3.00): \n"
        ).lower()
    

    # TODO add function to refill the machine perhaps this, off and report can \
    # only be handled by an admin with a password?