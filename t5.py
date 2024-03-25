# supplement for import
from random import randint
def roll_the_dice():
    return randint(1,7)


# Initialise the players
players = ["Red", "Blue", "Green", "White"]
positions = [0]

player_num = 0
while True:
    n = int(input("enter number of players."))
    for i in range(4-n):
        players.pop()
    print("positions", positions)
    if 0 > player_num > 4:
        print("The number of players must be 1 to 4")
    else:
        break
print("positions",positions)
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
p_rolls = [0]
new_roll = 0
p = 0
while p_rolls[len(p_rolls)-1] < 100:   
    new_roll += roll_the_dice()
    p_rolls.append(new_roll) 
    for num in range(len(players)):
        winner = ""            
        print("num", num)
        print(f"Player {players[num]} is in position X")   
        print("p_rolls", p_rolls)
        if p_rolls[len(p_rolls)-1] > 100:
            p_rolls.pop()
            new_roll = 0       
        else:
            print("new roll not over 100", new_roll)
            positions[num] = new_roll
            print("player position",positions[num])
            print("rolls",p_rolls)
                   
            if p_rolls[len(p_rolls)-1] in pre_alter:
                altered_p_position = post_alter[pre_alter.index(p_rolls[len(p_rolls)-1])]
                if p_rolls[len(p_rolls)-1] > altered_p_position:
                    print(f"Player {players[num]} stepped on a snake and is now in position {altered_p_position}")
                else:
                    print(f"Player {players[num]} climbed a ladder and is now in position {altered_p_position}")
                p_rolls[len(p_rolls)-1] = altered_p_position
            if p_rolls[len(p_rolls)-1] in pre_alter:
                altered_p_position = post_alter[pre_alter.index(p_rolls[len(p_rolls)-1])]
                if p_rolls[len(p_rolls)-1] > altered_p_position:
                    print(f"Player {players[num]} stepped on a snake and is now in position {altered_p_position}")
                else:
                    print(f"Player {players[num]} climbed a ladder and is now in position {altered_p_position}")
                p_rolls[len(p_rolls)-1] = altered_p_position
        winner = players[num]
        print("player played", players[num])
print("winner", winner)       