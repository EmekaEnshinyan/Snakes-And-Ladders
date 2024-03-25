from diceroll import roll_the_dice
from typing import Tuple

def initialise_game() -> Tuple[list, list, list, list, list, list]:
    
    # Initialise the players
    players = ["Red", "Blue", "Green", "White"]
    positions = [0] * len(players)

    # Initialise the snakes and ladders
    snake_heads = [25, 44, 65, 76, 99]
    snake_tails = [6, 23, 34, 28, 56]
    ladder_bases = [8, 26, 38, 47, 66]
    ladder_tops = [43, 39, 55, 81, 92]

    return players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops


def get_num_players() -> int:
    min_players = 1
    max_players = 4
    while True:
        num_players = int(input("How many players are playing (1, 2, 3 or 4)?: "))
        
        if not (num_players < min_players or num_players > max_players):
            break

    return num_players


def play_game(players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops) -> list:
    
    pre_alter = snake_heads + ladder_bases
    post_alter = snake_tails + ladder_tops

    turn = 0
    while True:
        if turn == len(players):
            turn = 0

        
        p_diceroll = roll_the_dice()

        # First - for each player, checking if the new position is less than, greater than, or equal to 100.
        # If less - it moves to the new position.
        # If greater - it passes (else statement).
        # If it is equal to 100, that player wins and the loop breaks so the next player cannot roll the dice.
        if positions[turn] + p_diceroll <= 100:
            positions[turn] += p_diceroll
            if positions[turn] == 100:
                break
        
        # Check if the player is either on a snake head or ladder Base
        # Update the positions if required
        if positions[turn] in pre_alter:
            positions[turn] = post_alter[pre_alter.index(positions[turn])]


        turn += 1

    return positions

def pick_winner(positions):
    winning_pos = 100
    if winning_pos not in positions:
        return -1
    else:   
        win_idx = positions.index(winning_pos)
    return win_idx


def main():
    players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops = initialise_game()
    num_players = get_num_players()
    
    players = players[:num_players]
    positions = positions[:num_players]

    final_positions = play_game(players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops)
    winner = pick_winner(final_positions)
    print(final_positions)
    print(f"The winner is {players[winner]}!")

if __name__ == '__main__':
    main()