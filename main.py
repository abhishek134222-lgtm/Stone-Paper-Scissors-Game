from game import game
from score import score
import utils

def main():
    print("             Welcome to the Game !!!")
    print("              Stone Paper Scissors")
    print("======================================================")
    utils.player_1 = input("Enter Player 1 Name: ")
    utils.player_2 = input("Enter Player 2 Name: ")   


    while True:
        print("Enter 1 to Start the Game")
        print("Enter 0 to Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1: 
            game()
        elif choice == 0:
            score()
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()