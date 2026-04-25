import utils
def score():
    print(f"Player 1 Score: {utils.score_1}")
    print(f"Player 2 Score: {utils.score_2}")
    if utils.score_1 > utils.score_2:
        print("So , Player 1 wins the game!")
    elif utils.score_2 > utils.score_1:
        print("So , Player 2 wins the game!")   
    else:
        print("The game is a tie!")

