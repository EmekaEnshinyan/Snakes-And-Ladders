# supplement for import
from random import randint
def roll_the_dice():
    return randint(1,6)

players = ["Red", "Blue", "Green", "White"]
positions = [0, 0, 0 , 0]
while True:
    n = int(input("enter number of players."))
    if n > 4:
        print("must be 1-4")
    else:
        for i in range(4-n):
            players.pop()
            positions.pop()
        break
print(players)
print(positions)

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
winner = ""
while winner == "":
    # roll dice and store in var
    for idx in range(len(positions)):
        dice_roll = roll_the_dice()
        print(f"Player {players[idx]} rolls the dice")
        #if positions[idx] < 100:
        if positions[idx] + dice_roll > 100:
            pass
        elif positions[idx] + dice_roll == 100:
            positions[idx] += dice_roll    
            winner = players[idx] 
            print(f"{winner} wins")
            break
        else:
            positions[idx] += dice_roll
            print(f"{players[idx]} is on {positions[idx]}")        
                     
            if positions[idx] in pre_alter:
                altered_position = post_alter[pre_alter.index(positions[idx])]
                if positions[idx] > altered_position:
                    print(f"Player {players[idx]} stepped on a snake and is now in position {altered_position}")
                else:
                    print(f"Player {players[idx]} climbed a ladder and is now in position {altered_position}")
                positions[idx] = altered_position         
                if positions[idx] in pre_alter:
                    altered_p2_position = post_alter[pre_alter.index(positions[idx])]
                    if positions[idx] > altered_p2_position:
                        print(f"Player {players[idx]} stepped on a snake and is now in position {altered_p2_position}")
                    else:
                        print(f"Player {players[idx]} climbed a ladder and is now in position {altered_p2_position}")
                    positions[idx] = altered_p2_position