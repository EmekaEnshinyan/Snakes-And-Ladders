import numpy as np
import t5 as task5

#player_list = [["Red", 0],["Blue", 100],["Green", 0],["White", 0]]
#snake_heads = [25, 44, 65, 76, 99]
#snake_tails = [6, 23, 34, 28, 56]
#ladder_bases = [8, 26, 38, 47, 66]
#ladder_tops = [43, 39, 55, 81, 92]    


def roll_the_dice():
    return np.random.randint(1, 7)


def initialize_game(player_list, snake_heads, snake_tails, ladder_bases, ladder_tops) -> list:
    return player_list, snake_heads, snake_tails, ladder_bases, ladder_tops
    
    
p_position = [0]
number_players = 0
def get_num_players(n) -> int:
    while True:
        n = int(input("enter number of players. The max number of players is 4\n"))
        number_players = n
        p_position*n
        if number_players > 4:
            print("too many players! Choose up to 4, please.")
        else:
            return n
            
#NOTICE player_list is a 2d array
def play_game(player_list, snake_heads, snake_tails, ladder_bases, ladder_tops) -> list:
    position = 1
    while True:
        for pos in player_list:
            if 100 in pos: 
                print("true")
        break

# Commence the game
    for pos in player_list:        
        while 100 not in pos:
            # Print the position for Player 1 and Player 2
            print(f"Player {pos[0]} is in position {pos[1]}")

            p1_diceroll = roll_the_dice()
            p2_diceroll = roll_the_dice()
            p1_position += p1_diceroll
            p2_position += p2_diceroll

            if p1_position > 100:
                pos[1] -= p1_diceroll
                p2_diceroll = roll_the_dice()
            if pos[1] > 100:
                pos[1] -= p2_diceroll
                p2_diceroll = roll_the_dice()
            print("player 1 rolls:", p1_diceroll, pos[1])
            print("player 2 rolls:", p2_diceroll, pos[1])

            # First - for each player, checking if the new position is less than, greater than, or equal to 100.
            # If less - it moves to the new position.
            # If greater - it passes (else statement).
            # If it is equal to 100, that player wins and the loop breaks so the next player cannot roll the dice.
    return 
    
def pck_winner(list) -> int:
    return 0