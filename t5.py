# DO NOT delete this line
from diceroll import roll_the_dice

min_players = 1
max_players = 4

players = ["Red", "Blue", "Green", "White"]
positions = [0 ,0, 0, 0]

while True:
    num_players = input("How many players are playing (1, 2, 3 or 4)?: ")
    # Checking the input is a digit, not letters:
    if not num_players.isdigit():
        print("please type the number of players from 1 to 4")
    else:
        num_players = int(num_players)
        # Verifiying valid number of players:
        if (num_players < min_players or num_players > max_players):
            print("please type the number of players from 1 to 4")
        else:
            # Upadting players and positions:
            players = players[:num_players]
            positions = positions[:num_players]
            break

# Initialise the snakes and ladders
snake_heads = [25, 44, 65, 76, 99]
snake_tails = [6, 23, 34, 28, 56]
ladder_bases = [8, 26, 38, 47, 66]
ladder_tops = [43, 39, 55, 81, 92]

pre_alter = snake_heads + ladder_bases
post_alter = snake_tails + ladder_tops

# Commence the game
turn = 0
while True:
    if turn == num_players:
        turn = 0

    if turn == 0:
        # Print the position for Player 1 and Player 2
        for player, position in zip(players, positions):
            print(f"Player {player} is in position {position}")
    
    p_diceroll = roll_the_dice()

    # First - for each player, checking if the new position is less than, greater than, or equal to 100.
    # If less - it moves to the new position.
    # If greater - it passes (else statement).
    # If it is equal to 100, that player wins and the loop breaks so the next player cannot roll the dice.
    if positions[turn] + p_diceroll <= 100:
        positions[turn] += p_diceroll
        if positions[turn] == 100:
            winner = players[turn]
            print(f"Player {winner} has reached 100 and is the winner!")
            break
    else:
        continue
    
    # Check if the player is either on a snake head or ladder Base

    # Update the positions if required

    # If the altered position is greater than the original, it is a ladder, otherwise it is a snake.
    if positions[turn] in pre_alter:
        altered_position = post_alter[pre_alter.index(positions[turn])]
        if positions[turn] > altered_position:
            print(f"Player {players[turn]} stepped on a snake and is now in position {altered_position}")
        else:
            print(f"Player {players[turn]} climbed a ladder and is now in position {altered_position}")
        positions[turn] = post_alter[pre_alter.index(positions[turn])]

    turn += 1
# Announce the winner -> In the loop