from coffee_data import MENU
from coffee_data import resources
from coffee_data import profit


# [x] TODO Handle Report
def handle_report():
    report = (f"Water: {resources['water']}\n"
                f"Milk: {resources['milk']}\n"
                f"Coffee: {resources['coffee']}")
    return report

# [x] TODO Check Resources
def check_resources(choice):
    missing_ingredients = []
    for ingredient in MENU[choice]["ingredients"]:
        amount_needed = MENU[choice]['ingredients'][ingredient]
        amount_left = resources[ingredient]
        if amount_needed > amount_left:
            missing_ingredients.append(ingredient)
    if len(missing_ingredients) == 0:
        return True, []
    else: 
        return False, missing_ingredients


# [x] TODO Make the coffee
def make_coffee(choice):
    for key in MENU[choice]["ingredients"]:
        if key in resources:
            updated_value = resources[key] - MENU[choice]["ingredients"][key]
            resources[key] = updated_value


# [x] TODO process coins
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
        return False, total, total_format, change
    elif total > cost:
        return True, total, total_format, change
    elif total == cost:
        return True, total, total_format, change


machine_on = True

while machine_on:

    user_choice = input(
        "What would you like to drink? "
        "(espresso $1.50/latte $2.50/cappuccino $3.00): \n"
        ).lower()

    if user_choice == "off":
        machine_on = False


    if user_choice == "report":
        print(handle_report())

    if user_choice in MENU:
        state, missing_ingredients = check_resources(user_choice)
        pennies = int(input("How many pennies? \n")) * 0.01
        nickels = int(input("How many nickles? \n")) * 0.05
        dimes = int(input("How many dimes? \n")) * 0.1
        quarters = int(input("How many quarters? \n")) * 0.25
        money_in, total, total_format, change = handle_payment(
                                                user_choice,
                                                quarters,
                                                dimes,
                                                nickels,
                                                pennies)
        if money_in and total == MENU[user_choice]["cost"]:
            make_coffee(user_choice)
            print(f"You inserted {total_format}. "
                    f"Your {user_choice.title()} is ready! Enjoy!")
        elif money_in and total > MENU[user_choice]["cost"]:
            make_coffee(user_choice)
            print(f"You inserted {total_format}. "
                    f"You're {user_choice.title()} is ready! Enjoy!\n"
                    f"Here's your change: ${change}")
        elif not money_in:
            print(f"You inserted {total_format}. "
                f"Sorry, {user_choice.title()} "
                f"costs ${MENU[user_choice]['cost']:.2f}\n"
                "Please try again")
    elif user_choice in MENU and not state:
        if len(missing_ingredients) > 1:
            format_missing_ingredents = ", ".join(missing_ingredients[:-1])
            + " and " + missing_ingredients[-1]
            print(f"Sorry we are out of {format_missing_ingredents}")
        elif len(missing_ingredients) == 1:
            print(f"Sorry we are out of {missing_ingredients[0]}")
    elif user_choice not in MENU and user_choice != "off" and user_choice != "report":
        print("Please enter a valid option.")


    # [ ] TODO add function to refill the machine perhaps this, off and report can 
    # only be handled by an admin with a password?

    # [ ] TODO Fix error handling for empty resources. When resource empty, else
    # block runs.

    # [ ] TODO Fix bug with report and off command, returns KeyError: '{value}'
    # It seems to be checking for off or report in check_resources meaning regardless of my precondition check, it's 
    # bypassing and still running the main logic in the main loop.