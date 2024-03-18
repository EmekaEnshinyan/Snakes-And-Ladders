# supplement for import
from random import randint
def roll_the_dice():
    return randint(1,12)


# Initialise the players
#Red -> Blue -> Green -> White
player_list = [["Red", 0],["Blue", 100],["Green", 0],["White", 0]]
p_position = [0]

number_players = 0
while True:
    n = int(input("enter number of players. The max number of players is 4\n"))
    number_players = n
    p_position*n
    if number_players > 4:
        print("too many players! Choose up to 4, please.")
    else:
        break
# get num of players
    # get value of of index [0][1] for each player
        # 

# Initialise the snakes and ladders
snake_heads = [25, 44, 65, 76, 99]
snake_tails = [6, 23, 34, 28, 56]
ladder_bases = [8, 26, 38, 47, 66]
ladder_tops = [43, 39, 55, 81, 92]
pre_alter = snake_heads + ladder_bases
post_alter = snake_tails + ladder_tops
print(pre_alter)
print(post_alter)

# testing
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
        print(f"Player {pos[0]} is in position {p1_position}\nPlayer {p2_name} is in position {p2_position}")

        p1_diceroll = roll_the_dice()
        p2_diceroll = roll_the_dice()
        p1_position += p1_diceroll
        p2_position += p2_diceroll

        if p1_position > 100:
            p1_position -= p1_diceroll
            p2_diceroll = roll_the_dice()
        if p2_position > 100:
            p2_position -= p2_diceroll
            p2_diceroll = roll_the_dice()
        print("player 1 rolls:", p1_diceroll, p1_position)
        print("player 2 rolls:", p2_diceroll, p2_position)

        # First - for each player, checking if the new position is less than, greater than, or equal to 100.
        # If less - it moves to the new position.
        # If greater - it passes (else statement).
        # If it is equal to 100, that player wins and the loop breaks so the next player cannot roll the dice.
        if pos[1] == 100:
            print(f"Player {pos[0]} has reached 100 and is the winner!")
        # Check if player 1 is either on a snake head or ladder Base

        # Check if player 2 is either on a snake head or ladder Base

        # Update the positions if required
        # If the altered position is greater than the original, it is a ladder, otherwise it is a snake.
        if p1_position in pre_alter:
            altered_p1_position = post_alter[pre_alter.index(p1_position)]
            if p1_position > altered_p1_position:
                print(f"Player {pos[0]} stepped on a snake and is now in position {altered_p1_position}")
            else:
                print(f"Player {pos[0]} climbed a ladder and is now in position {altered_p1_position}")
            p1_position = altered_p1_position

        if p2_position in pre_alter:
            altered_p2_position = post_alter[pre_alter.index(p2_position)]
            if p2_position > altered_p2_position:
                print(f"Player {pos[0]} stepped on a snake and is now in position {altered_p2_position}")
            else:
                print(f"Player {pos[0]} climbed a ladder and is now in position {altered_p2_position}")
            p2_position = altered_p2_position
                