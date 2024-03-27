# Import
from diceroll import roll_the_dice

# Parameters
players = ["Red", "Blue", "Green", "White"]
positions = [0, 0, 0 , 0]

min_players = 1
max_players = 4

# Getting players' input for number of players
while True:
    num_players = input(f"How many players are playing ({min_players}-{max_players})?: ")
    # Checking the input is a digit, not letters:
    if not num_players.isdigit():
        print(f"Please type the number of players from {min_players} to {max_players}")
    else:
        num_players = int(num_players)
        # Verifiying valid number of players:
        if (num_players < min_players or num_players > max_players):
            print(f"Please type the number of players from {min_players} to {max_players}")
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
winner = ""
while winner == "":
    # Looping through players
    for idx in range(len(positions)):
        # roll dice and store in var
        dice_roll = roll_the_dice()
        print(f"Player {players[idx]} rolls the dice")
        # Skipping if a pleyer's crossing 100
        if positions[idx] + dice_roll > 100:
            pass
        # updating position if the new position is valid (<=100)
        # and declaring winner if there is one
        elif positions[idx] + dice_roll == 100:
            positions[idx] += dice_roll    
            winner = players[idx] 
            print(f"Player {winner} has reached 100 and is the winner!")
            break
        else:
            positions[idx] += dice_roll
            print(f"{players[idx]} is on {positions[idx]}")        
            # checking for ladders or snakes         
            if positions[idx] in pre_alter:
                altered_position = post_alter[pre_alter.index(positions[idx])]
                if positions[idx] > altered_position:
                    print(f"Player {players[idx]} stepped on a snake and is now in position {altered_position}")
                else:
                    print(f"Player {players[idx]} climbed a ladder and is now in position {altered_position}")
                positions[idx] = post_alter[pre_alter.index(positions[idx])]        