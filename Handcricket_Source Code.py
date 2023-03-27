#importing random to get random values
import random

# function to check if the input from user is valid or not
def is_valid_input(user_input):
    if user_input.isdigit() and int(user_input) >= 0 and int(user_input) <= 6:
        return True
    else:
        return False

# function to play one innings of hand cricket game
def play_innings():
    user_score = 0
    computer_score = 0
    print("Your turn to bat.")
    while True:
        user_input = input("Enter your choice (0-6): ")
        if is_valid_input(user_input):
            user_choice = int(user_input)
            computer_choice = random.randint(0, 6)
            print("Computer chose: ", computer_choice)
            if user_choice == computer_choice:
                print("Out! Your score is: ", user_score)
                break
            else:
                user_score += user_choice
                print("Your score is: ", user_score)
        else:
            print("Invalid input! Please enter a number between 0 and 6.")
    print("Computer's target is: ", user_score+1)
    print("Computer's turn to bat.")
    while True:
        computer_choice = random.randint(0, 6)
        user_input = input("Enter your choice (0-6): ")
        if is_valid_input(user_input):
            user_choice = int(user_input)
            print("Computer chose: ", computer_choice)
            if user_choice == computer_choice:
                print("Out! Computer's score is: ", computer_score)
                break
            else:
                if computer_score <= user_score:
                    computer_score += computer_choice
                    print("Computer's score is: ", computer_score)
                else:
                    print("Computer Wins!")
                    break
        else:
            print("Invalid input! Please enter a number between 0 and 6.")
    if user_score > computer_score:
        print("You win by", user_score-computer_score, "runs!" )
    elif computer_score == user_score:
        print("Match tied")
    else:
        print("Better luck next time!")
# main program
print("Welcome to Hand Cricket!")
play_innings()