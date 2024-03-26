# DO NOT delete this line
from random import randint

def roll_the_dice():
    return randint(1,6)

# Initialise the players
p1_name = "Red"
# Player 1 Position
p1_position = 0
# Player 2 Name
p2_name = "Blue"
# Player 2 Position
p2_position = 0
# Initialise the snakes and ladders
snake_heads = [25, 44, 65, 76, 99]
snake_tails = [6, 23, 34, 28, 56]
ladder_bases = [8, 26, 38, 47, 66]
ladder_tops = [43, 39, 55, 81, 92]
pre_alter = snake_heads + ladder_bases
post_alter = snake_tails + ladder_tops
print(pre_alter)
print(post_alter)


# Commence the game
roll = 0
proxy1_pos = 0
p1_pos = 0
while True:
    print(f"Player {p1_name} is in position {p1_position}")
    print(f"Player {p2_name} is in position {p2_position}")
    p1_diceroll = roll_the_dice()
    p2_diceroll = roll_the_dice()   
    
    '''
    - get dice roll
        - add diceroll to a var that will accumulate the rolls
            - set p1 position to var, unless it exceeds 100
                - if exceeds 100, then ignore roll and declare p1 winner
    '''
    # player 1 rolls  
    # TODO: make sure align with assignment cond        
    if p1_position + p1_diceroll > 100:
        pass
    elif p1_position + p1_diceroll == 100:
        p1_position += p1_diceroll
        winner = p1_name
        print(f"{winner} wins")
        # break terminates the loop
        break
    else:
        p1_position += p1_diceroll
        
    if p2_position + p2_diceroll > 100:
        pass
    elif p2_position + p2_diceroll == 100:
        p2_position += p2_diceroll
        winner = p2_name
        print(f"{winner} wins")
        break
    else:
        p2_position += p2_diceroll
    
    # snakes & ladders
    if p1_position in pre_alter:
        altered_p1_position = post_alter[pre_alter.index(p1_position)]
        if p1_position > altered_p1_position:
            print(f"Player {p1_name} stepped on a snake and is now in position {altered_p1_position}")
        else:
            print(f"Player {p1_name} climbed a ladder and is now in position {altered_p1_position}")
        p1_position = altered_p1_position

    if p2_position in pre_alter:
        altered_p2_position = post_alter[pre_alter.index(p2_position)]
        if p2_position > altered_p2_position:
            print(f"Player {p2_name} stepped on a snake and is now in position {altered_p2_position}")
        else:
            print(f"Player {p2_name} climbed a ladder and is now in position {altered_p2_position}")
        p2_position = altered_p2_position
        
