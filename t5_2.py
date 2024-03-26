# TODO: careful with conflation of vars

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
#OBJECTS: ["player1", "player2", ...]; [0, 0, ...]

''''''
# Initialise the snakes and ladders
snake_heads = [25, 44, 65, 76, 99]
snake_tails = [6, 23, 34, 28, 56]
ladder_bases = [8, 26, 38, 47, 66]
ladder_tops = [43, 39, 55, 81, 92]
pre_alter = snake_heads + ladder_bases
post_alter = snake_tails + ladder_tops
print(pre_alter)
print(post_alter)
# OBJECTS: [25, 44, 65, 76, 99,8, 26, 38, 47, 66]; [6, 23, 34, 28, 56, 43, 39, 55, 81, 92]

# Commence the game

while winner == "":
    winner = ""
    # roll dice and store in var
    place = 0
    dice_roll = roll_the_dice()
    for position in positions:
        p = 0
        print(p)
        print(f"Player {players[place]} rolls the dice")
        if p < 100:
            p += dice_roll
            position = p
            print(p)
            place += 1
        elif p + dice_roll == 100:
            winner = players[place]
            print(f"The winner is {winner}!")
            break
        elif p + dice_roll > 100:
            pass
                
'''
    for position in positions:
        if position <= 100:
            position += dice_roll
        elif position + dice_roll == 100:
            print(f"Player {players[place]} is in position {positions[place]}")
            break
        else:
            pass
'''
'''
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
'''

'''
        - get # of players where # = n
            - for each n, n rolls dice
                -
'''

'''
    print("dice rolled", new_roll)

    for num in range(len(players)):
        print(f"Player {players[num]} is in position {positions[num]}")
        print("p_rolls", p_rolls)
            break



    if p_rolls[len(p_rolls)-1] > 100:
            p_rolls.pop()
            new_roll = 0
        else:
            print("new roll not over 100", new_roll)
            positions[num] = new_roll
            print("player position",positions[num])
            print("rolls",p_rolls)
'''