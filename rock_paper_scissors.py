import random

options = ['Rock', 'Paper', 'Scissors']

comp_choice = random.randint(0, 2)
user_choice = int(input("Enter 0 for Rock, 1 for Paper or 2 for Scissors:\n"))

if user_choice < 0 and user_choice > 2:
    print("Invalid choice, please try again")

if comp_choice == user_choice:
    print("Game Tied")
elif comp_choice % 2:
    print(
        f"Computer chose {options[comp_choice]} and you chose {user_choice}. You lose!"
        )