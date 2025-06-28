import coffee_data

resources = coffee_data.resources
MENU = coffee_data.MENU


def handle_report():
    report = (f"Water: {resources['water']}\n"
    f"Milk: {resources['milk']}\n"
    f"Coffee: {resources['coffee']}")
    return report


# TODO check if resources are sufficient
def check_resources(choice):
    missing_ingredients = []
    for ingredient in coffee_data.MENU[choice]["ingredients"]:
        amount_needed = coffee_data.MENU[choice]['ingredients'][ingredient]
        amount_left = coffee_data.resources[ingredient]
        if amount_needed > amount_left:
            missing_ingredients.append(ingredient)
    
    if len(missing_ingredients) > 0:
        missing_ingredients_formatted = ", ".join(missing_ingredients[:-1]) + " and " + missing_ingredients[-1]

        return f"Sorry, we don't have enough {missing_ingredients_formatted}."
    else:
        return make_coffee(choice)


# TODO Make the coffee
def make_coffee(choice):
    # updated_value = []
    for key in MENU[choice]["ingredients"]:
        if key in resources:
            # resources.update(resources - MENU[choice]["ingredients"])
            updated_value = resources[key] - MENU[choice]["ingredients"][key]
            resources[key] = updated_value
    print(resources)
    return f"Your {choice} is ready! Enjoy carefully as products are hot!"

    
    # When the user chooses their drink, deduct rources needed from current resources in coffee_data.py
    # How do I do that?
    # resources available - resources needed
    
    # resources - choice[ingredients]


# TODO process coins
def handle_payment():
    pass
    # TODO check if transaction is successful, if too much money, return change


machine_on = True

while machine_on:
    user_choice = input(
        "What would you like to drink? (espresso/latte/cappuccino): \n").lower()

    # TODO Thank user for using coffemaker deluxe v10.0

    if user_choice in MENU:
        # check_resources(user_choice)
        print(check_resources(user_choice))
        print(handle_report())
    elif user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        print(handle_report())
    # TODO fix error with user_choice = off caused by check_resources
    # if user_choice == "off":
    #     machine_on = False

    # if user_choice == "report":
    #     print(handle_report())



    # result = check_resources(user_choice)
    # done = make_coffee(user_choice)

    # print(result)
    # print(done)