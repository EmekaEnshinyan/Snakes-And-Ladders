from diceroll import roll_the_dice, special_roll
from helpers import generate_surprises

def initialise_game() -> dict:
        
    # Initialise the players
    
    game_params = {
        "players": {"Red": 0, "Blue": 0, "Green": 0, "White": 0},
        "snakes": {"25": 6, "44":23, "65":34, "76":28, "99":56},
        "ladders": {"8": 43, "26": 39, "38": 55, "47": 81, "66": 92}
    }

    return game_params


def get_num_players() -> int:
    min_players = 1
    max_players = 4

    while True:
        num_players = int(input("How many players are playing (1, 2, 3 or 4)?: "))
    
        if not (num_players < min_players or num_players > max_players):
            break

    return num_players


def play_game(game: dict) -> str:
    # Adding surprise tiles.
    game["surprise_tiles"] = generate_surprises()
    # Crearing a list of snake heads and ladder bases: 
    pre_alter = list(game["snakes"].keys()) + list(game["ladders"].keys())
    # Converting all elements to int.
    pre_alter = list(map(int, pre_alter))
    # Crearing a list of snake tails and ladder tops: 
    post_alter = list(game["snakes"].values()) + list(game["ladders"].values())
    # Getting players names.
    player_names = list(game["players"].keys())

    # 'turn' is used to loop through players throughout the while loop.
    turn = 0 
    while True:

        # Taking turn between players. 
        # If we reach the end of the list of players, or skip beyond it
        # due to a special dice roll, the turn is updated back.
        if turn >= len(game["players"]):
            # For one player games only, skipping turns won't work,
            # so we need to reset it.
            if len(game["players"]) == 1: 
                turn = 0
            else:
                turn -= len(game["players"])
        # Taking the name of the current player (i.e. the one who plays
        # the current turn), then rolling the dice.
        current_player = player_names[turn]
        p_diceroll = roll_the_dice()

        # Updating position if not passing 100.
        if game["players"][current_player] + p_diceroll <= 100:
            game["players"][current_player] += p_diceroll
            # Checking for victory.
            if game["players"][current_player] == 100:
                break # Loop breaks when a player wins.
        
        # Update position if stepped on a snake head or a ladder base:    
        if game["players"][current_player] in pre_alter:
            game["players"][current_player] = post_alter[pre_alter.index(game["players"][current_player])]
        
        # Checking if the player's position is on a surprise tile:
        if game["players"][current_player] in game["surprise_tiles"]:
            new_roll = special_roll()
            
            if new_roll == 0:
                # Not updating 'turn', continuing for another iteration
                # with the same player.
                continue

            elif new_roll == 1:
                # Skipping turn: updating turn and skipping to the next
                # iteration.
                turn += 2
                continue

            elif new_roll == 2:
                # Creating a set of names without the current player's name.
                players_to_update = set(game["players"].keys()) - {current_player}
                # Looping through the players sans the current, and
                # moving them back 5 spots, unless, if they're too close
                # to 0, then the players are moved to 0.
                for player_to_update in players_to_update:
                    game["players"][player_to_update] -= 5
                    if game["players"][player_to_update] < 0:
                        game["players"][player_to_update] = 0

        # If the loop neither breaks nor continues, then 'turn' is 
        # updated and the game goes on.
        turn += 1
    # Picking the winner.
    winner = pick_winner(game["players"])
    return winner


def pick_winner(players: dict) -> str:
    winning_pos = 100

    if winning_pos not in players.values():
        return None
    else:   
        win_idx = list(players.values()).index(winning_pos)
        winner = list(players.keys())[win_idx]

    return winner

def turn_by_turn_gameplay():
    # Setting to a fixed number of players
    num_players = 2 

    game = initialise_game()
    game["players"] = dict(list(game["players"].items())[:num_players])
    
    # Adding surprise tiles.
    game["surprise_tiles"] = generate_surprises()
    # Crearing a list of snake heads and ladder bases: 
    pre_alter = list(game["snakes"].keys()) + list(game["ladders"].keys())
    # Converting all elements to int.
    pre_alter = list(map(int, pre_alter))
    # Crearing a list of snake tails and ladder tops: 
    post_alter = list(game["snakes"].values()) + list(game["ladders"].values())
    # Getting players names.
    player_names = list(game["players"].keys())

    # 'turn' is used to loop through players throughout the while loop.
    turn = 0 
    while True:

        # Taking turn between players. 
        # If we reach the end of the list of players, or skip beyond it
        # due to a special dice roll, the turn is updated back.
        if turn >= len(game["players"]):
            turn -= len(game["players"])
        # Taking the name of the current player (i.e. the one who plays
        # the current turn), then rolling the dice.
        current_player = player_names[turn]

        # This is the "turn by turn" component.
        while True:
            choice = input(f"{current_player}, would you like to roll or quit? ")
            if choice == "roll":
                break
            elif choice == "quit":
                winner = pick_winner(game["players"])
                return winner
            else:
                print("You need to type either 'roll' or 'quit'.")

        p_diceroll = roll_the_dice()

        # Updating position if not passing 100.
        if game["players"][current_player] + p_diceroll <= 100:
            game["players"][current_player] += p_diceroll
            # Checking for victory.
            if game["players"][current_player] == 100:
                break # Loop breaks when a player wins.
        
        # Update position if stepped on a snake head or a ladder base:    
        if game["players"][current_player] in pre_alter:
            game["players"][current_player] = post_alter[pre_alter.index(game["players"][current_player])]
        
        # Checking if the player's position is on a surprise tile:
        if game["players"][current_player] in game["surprise_tiles"]:
            new_roll = special_roll()
            
            if new_roll == 0:
                # Not updating 'turn', continuing for another iteration
                # with the same player.
                continue

            elif new_roll == 1:
                # Skipping turn: updating turn and skipping to the next
                # iteration.
                turn += 2
                continue

            elif new_roll == 2:
                # Creating a set of names without the current player's name.
                players_to_update = set(game["players"].keys()) - {current_player}
                # Looping through the players sans the current, and
                # moving them back 5 spots, unless, if they're too close
                # to 0, then the players are moved to 0.
                for player_to_update in players_to_update:
                    game["players"][player_to_update] -= 5
                    if game["players"][player_to_update] < 0:
                        game["players"][player_to_update] = 0

        # If the loop neither breaks nor continues, then 'turn' is 
        # updated and the game goes on.
        turn += 1
    # Picking the winner.
    winner = pick_winner(game["players"])
    return winner

def main():
    game_init = initialise_game()

    # Slicing dictionary according to number of players.
    game_init["players"] = dict(list(game_init["players"].items())[:get_num_players()])

    winner = play_game(game_init)
    if winner:
        print(f"The winner is {winner}!")
    else:
        print(f"No winner this time")

    # Play a turn by turn game
    winner = turn_by_turn_gameplay()
    if winner:
        print(f"The winner is {winner}!")
    else:
        print(f"Well... guess you're not much into playing anymore...")

if __name__ == '__main__':
    main()