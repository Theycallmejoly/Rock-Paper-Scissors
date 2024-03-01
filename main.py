import random

user_wins = 0 
computer_wins = 0

options = ["rock", "paper", "scissors"]

def askingFunc():
    while True:
        user_choice = input("Type Rock, Paper, or Scissors (Type 'Q' to exit): ").lower()
        if user_choice == "q":
            return user_choice
        elif user_choice not in options:
            print("Please type Rock, Paper, or Scissors!")
            continue
        else:
            return user_choice

while True:
    user_choice = askingFunc()

    if user_choice == "q":
        break

    random_number = random.randint(0, 2)
    computer_choice = options[random_number]
    print("Computer's choice is", computer_choice + ". ")

    if computer_choice == user_choice:
        print("It's a tie!")
    elif (computer_choice == "rock" and user_choice == "scissors") or \
         (computer_choice == "paper" and user_choice == "rock") or \
         (computer_choice == "scissors" and user_choice == "paper"):
        print("Unlucky mate! You lost!")
        computer_wins += 1
    else:
        print("Congrats! You won.")
        user_wins += 1

    play_again = input("Do you want to play again? (Y/N): ").lower()
    if play_again != "y":
        break

print("Total wins - You:", user_wins, "Computer:", computer_wins)
print("Goodbye!")
