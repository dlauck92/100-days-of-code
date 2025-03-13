# Rock, Paper, Scissors Game
import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer_choice = random.randint(0, 2)
print(f"The computer chose {computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("Computer Wins!")
elif computer_choice > user_choice:
    print("Computer Wins!")
elif user_choice > computer_choice:
    print("You win!")    
elif user_choice == computer_choice:
    print("Draw!")
elif user_choice > 2:
    print("Please select ")
else:
    print("Please try a valid number.")