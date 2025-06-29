# This function checks if resources are available. Keeping here while refactoring.
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
        return handle_payment(choice, quarters, dimes, nickels, pennies)


# This function makes the coffe and updates resources (split this function maybe?). Keeping here while refactoring
def make_coffee(choice):
    # updated_value = []
    for key in MENU[choice]["ingredients"]:
        if key in resources:
            # resources.update(resources - MENU[choice]["ingredients"])
            updated_value = resources[key] - MENU[choice]["ingredients"][key]
            resources[key] = updated_value
    print(resources)
    return f"Your {choice} is ready! Enjoy carefully as products are hot!"


# This function handles payments. Keeping here while refactoring
def handle_payment(choice, quarters, dimes, nickels, pennies):
    choice_cost = MENU[choice]["cost"]
    total = quarters + dimes + nickels + pennies
    total_format = f"${quarters + dimes + nickels + pennies:.2f}"
    if total < choice_cost:
        return f"Your total is {total_format}. Sorry that's not enough money. Transaction cancelled."
    elif total >= choice_cost:
        if total == choice_cost:
            return f"Your total is {total_format}. {make_coffee (choice)}."
        elif total > choice_cost:
            return f"Your total is {total_format}. {make_coffee (choice)}. Heres is ${total - choice_cost:.2f} in change."
    else:
        # Figure this our later
        pass


# This is the main logic inside of my loop. Keeping here while refactoring
    # if user_choice in MENU:
    #     quarters = int(input("How many quarters?: \n")) * 0.25 
    #     dimes = int(input("How many dimes?: \n")) * 0.10
    #     nickels = int(input("How many nickels?: \n")) * 0.05
    #     pennies = int(input("How many pennies?: \n")) * 0.01
    #     print(check_resources(user_choice))
    # elif user_choice == "off":
    #     machine_on = False
    # elif user_choice == "report":
    #     print(handle_report())