import coffee_data

resources = coffee_data.resources

def handle_report():
    report = (f"Water: {resources['water']}\n"
    f"Milk: {resources['milk']}\n"
    f"Coffee: {resources['coffee']}")
    return report

def check_resources():
    



machine_on = True

while machine_on:
    user_choice = input("What would you like to drink? (espresso/latte/cappuccino): \n").lower()

    # TODO check if resources are sufficient

    # TODO process coins

    # TODO check if transaction is successful, if too much money, return change

    # TODO Make the coffee

    # TODO Thank user for using coffemaker deluxe v10.0

    if user_choice == "report":
        print(handle_report())

    if user_choice == "off":
        machine_on = False