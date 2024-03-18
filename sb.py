from random import randint
def roll_the_dice():
    return randint(1,12)


# Initialise the players
#Red -> Blue -> Green -> White
p_list = [["Red", 3],["Blue", 5],["Green", 7],["White", 100]]
p_position = [0]

while True:
    n = int(input("enter number of players. The max number of players is 4\n"))
    p_position *= n
    print(p_position)
    if len(p_position) > 4:
        print("too many players! Choose up to 4, please.")
    else:
        for i in range(len(p_position)):
            print(f"Player {p_list[i][0]} is in position {p_position[0]}")    
    break

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
for pos in p_list:
    c = 1
    print("p nums, position", pos[c])
    c += 1

while True:
    for pos in p_list:
        if 100 not in pos:
            diceroll = roll_the_dice()
            c = 0
            pos[1] += diceroll
            if pos[1] > 100:
                pos[1] -= diceroll
                diceroll = roll_the_dice()
            print(f"Player {pos[0]} is in position {pos[1]}\n")
            c += 1
        elif 100 in pos:
            winner = ''
            winner = pos[pos.index(100)-1]
            print("winner index", winner)
            print(f"{pos[pos.index(100)]} wins")            
            break
    break            
            
            
'''
    
    
    if p1_position > 100:
        p1_position -= p1_diceroll
        p2_diceroll = roll_the_dice()
    if p2_position > 100:
        p2_position -= p2_diceroll
        p2_diceroll = roll_the_dice()
    print("player 1 rolls:", p1_diceroll, p1_position)
    print("player 2 rolls:", p2_diceroll, p2_position)

'''
            
            
            

