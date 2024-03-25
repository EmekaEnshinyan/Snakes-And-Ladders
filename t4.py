'''
For this task, we are restricting 
where you can place the Snakes and Ladders, so please follow along: 
'''

# DO NOT delete this line
from random import randint

def roll_the_dice():
    return randint(1,7)

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
p1_rolls = []
p2_rolls = []
new_roll = 0
while p1_position != 100 or p2_position != 100:
    print(f"Player {p1_name} is in position {p1_position}\nPlayer {p1_name} is in position {p2_position}")
    p1_diceroll = roll_the_dice()
    p2_diceroll = roll_the_dice()    
         
    new_roll += p1_diceroll
    if p1_position + new_roll >= 100:
        winner = f"Player {p1_name} has reached 100 and is the winner!"
        print(winner)
        break
    print("new roll", new_roll)
    p1_rolls.append(new_roll)
    if p1_rolls[len(p1_rolls)-1] > 100:
        p1_rolls.pop()
    else:
        p1_position += new_roll
    new_roll = 0
    if p2_position + new_roll >= 100:
        winner = f"Player {p2_name} has reached 100 and is the winner!"
        print(winner)
        break
    
    print("post roll", p1_rolls)     
    new_roll += p2_diceroll
    p2_rolls.append(new_roll)
    if p2_rolls[len(p2_rolls)-1] > 100:
        p2_rolls.pop()
    else:
        p2_position += new_roll
    new_roll = 0
       
    
    

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
        
