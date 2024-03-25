#from diceroll import roll_the_dice, special_roll
#from helpers import generate_surprises
from random import randint

#players = ["Red", "Blue", "Green", "White"]
#positions = [0, 0, 0 , 0]
#snake_heads = [25, 44, 65, 76, 99]
#snake_tails = [6, 23, 34, 28, 56]
#ladder_bases = [8, 26, 38, 47, 66]
#ladder_tops = [43, 39, 55, 81, 92]    

players = {"Red": 0, "Blue": 0, "Green": 0, "White": 0}
snakes = {25: 6, 44: 23, 65: 34, 76: 28, 99: 56}
ladders = {8: 43, 6: 39, 38: 55, 47: 81, 66: 92}
   
def roll_the_dice():
    return randint(1,6)

def initialise_game() -> dict:
    return players, snakes, ladders
   

def get_num_players() -> int:
    while True:
      n = int(input("enter number of players."))
      if n > 4:
          print("must be 1-4")
      else:
          return 0
      return n

def play_game(game: dict) -> str:
    pass

def pick_winner(players: dict) -> str:
    pass

def turn_by_turn_gameplay():
    pass

def main():
    game = initialise_game()
    num_players = get_num_players()
    winner = play_game(game)
    print(f"The winner is {winner}!")

    # Play a turn by turn game
    turn_by_turn_gameplay()

if __name__ == '__main__':
    main()