import random

def game():
    options = ["r", "p", "s"]
    while True:
        choice = input("Enter r for rock, p for paper or s for scissors (or quit to leave the game)")

        if choice == "quit":
            break

        if choice not in options:
            print("Invalid")
            continue

        computer_choice = random.choice(options)
        print(f"The Computer choose: {computer_choice}")

        if choice == computer_choice:
            print("Its a tie")

        elif (choice == "r" and computer_choice == "s") or \
            (choice == "p" and computer_choice == "r") or \
            (choice == "s" and computer_choice == "p"):
            print("You win")
        else:
            print("You lose")

if __name__ == "__main__":
    game()