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
        return True, []
    else: 
        return False, missing_ingredients


def make_coffee(choice):
    for key in MENU[choice]["ingredients"]:
        if key in resources:
            updated_value = resources[key] - MENU[choice]["ingredients"][key]
            resources[key] = updated_value


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

def input_validation(prompt, denomination):
    while True:
        user_payment = input(prompt)
        try:
            return int(user_payment) * denomination
        except ValueError:
            print("Please enter a valid number")


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
        if state and len(missing_ingredients) == 0:
            pennies_multi = 0.01
            nickels_multi = 0.05
            dimes_multi = 0.1
            quarters_multi = 0.25

            pennies = input_validation(
                                    "How many pennies? \n"
                                    , pennies_multi)
            nickels = input_validation(
                                    "How many nickels? \n"
                                    , nickels_multi)
            dimes = input_validation(
                                    "How many dimes? \n"
                                    , dimes_multi)
            quarters = input_validation(
                                    "How many quarters? \n"
                                    , quarters_multi)

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
                        f"Your {user_choice.title()} is ready! Enjoy!\n"
                        f"Here's your change: ${change}")
            elif not money_in:
                print(f"You inserted {total_format}. "
                    f"Sorry, {user_choice.title()} "
                    f"costs ${MENU[user_choice]['cost']:.2f}\n"
                    "Please try again")
        elif user_choice in MENU and not state:
            if len(missing_ingredients) > 1:
                format_missing_ingredients = (", ".join(missing_ingredients[:-1])
                                            + " and "
                                            + missing_ingredients[-1])
                print(f"Sorry we are out of {format_missing_ingredients}")
            elif len(missing_ingredients) == 1:
                print(f"Sorry we are out of {missing_ingredients[0]}")
    elif user_choice not in MENU and user_choice != "off" and user_choice != "report":
        print("Please enter a valid option.")


    # [ ] TODO add function to refill the machine perhaps this, off and report can 
    # only be handled by an admin with a password?

    # [ x ] TODO Fix error handling for empty resources. When resource empty, else
    # block runs.