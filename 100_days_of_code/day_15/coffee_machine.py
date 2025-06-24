import coffee_data

run = True

while run:
    user_choice = input("What would you like to drink? (espresso/latte/cappuccino): \n").lower()

    if user_choice == "off":
        run = False

    if user_choice == "report":
        # TODO generate report showing current resource values
        pass

    # TODO check if resources are sufficient

    # TODO process coine

    # TODO check if transaction is successful
        # if too much money, return change

    # TODO Make the coffee

    # Thank user for using coffemaker deluxe v10.0 