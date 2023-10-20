import random
# to get user choice function
def get_user_choice():
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
# to get computer's choice function
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# to determin the winner it contains all decisions for winning the game
def findOut_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        return "You won!"
    else:
        return "Computer won!"

# main function
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")
    result = findOut_winner(user_choice, computer_choice)
    print(result)
        
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break
