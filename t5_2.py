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
print("players & Positions", players, positions)
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
p_rolls = [0]
check_positions = positions
new_roll = 0
while p_rolls[len(p_rolls)-1] < 100:   
    place = 0
    for position in positions:
        print(f"Player {players[place]} is in position {positions[place]}")   
        print(f"Player {players[place]} rolls the dice")   
        p_rolls.append(roll_the_dice())
        #positions[place] += p_rolls[place]
        check_positions[place] += p_rolls[place]
        print(f"{players[place]} position", p_rolls[(len(p_rolls)-1)])
        if check_positions[place] > 100:
            print(f"{players[place]} wins")
            break
        else:
            positions[place] += p_rolls[(len(p_rolls)-1)]
            print("roll 3", p_rolls)
            print("positions",positions)
            print(f"{players[place]} at {positions[place]}")
            place += 1
    print(p_rolls)
    print(positions)
    
        
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