import random as r
import utils
def game():
    utils.player_1_got = r.choice(utils.choose)
    utils.player_2_got = r.choice(utils.choose)

    if utils.player_1_got == utils.player_2_got:
        print("Both players got the same. It's a tie!")

    elif (utils.player_1_got == "Stone" and utils.player_2_got == "Scissors"):
        print("Player 1 wins! Stone crushes Scissors.")
        utils.score_1 += 1
    elif (utils.player_1_got == "Paper" and utils.player_2_got == "Stone"):
        print("Player 1 wins! Paper covers Stone.")
        utils.score_1 += 1
    elif (utils.player_1_got == "Scissors" and utils.   player_2_got == "Paper"):
        print("Player 1 wins! Scissors cut Paper.")
        utils.score_1 += 1
    else:
        print(f"Player 2 wins! {utils.player_2_got} beats {utils.player_1_got}.")
        utils.score_2 += 1

