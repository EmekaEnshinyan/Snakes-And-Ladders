import numpy as np

players = ["Red", "Blue", "Green", "White"]
positions = [0, 0, 0, 0]
snake_heads = [25, 44, 65, 76, 99]
snake_tails = [6, 23, 34, 28, 56]
ladder_bases = [8, 26, 38, 47, 66]
ladder_tops = [43, 39, 55, 81, 92]    


def roll_the_dice():
    return np.random.randint(1, 6)

def initialize_game() -> list:
    return players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops
    

def get_num_players() -> int:
   n = 0 
   while True:
    n = int(input("enter number of players."))
    if n > 4:
        print("must be 1-4")
    else: 
        return n
    

# final num of player positions
def play_game(players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops) -> list:
    
    p_rolls = [0]
    check_positions = positions
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
    
def pck_winner(list) -> int:
    
    return 0


'''
TESTING GROUND
'''
def add_number():
    return 5
x = get_num_players()
y = add_number()
print(x+y)

'''
def main():
    players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops = initialise_game()
    
    final_positions = play_game(players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops)
    
    winner = pick_winner(final_positions)
    print(f"The winner is {players[winner]}!")

if __name__ == '__main__':
    main()
'''