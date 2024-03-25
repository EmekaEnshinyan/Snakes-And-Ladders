# Copy and paste everything from Task2
# DO NOT delete this line
from diceroll import roll_the_dice
from random import choice, choices

# Copy and paste the work from Task 1 here 


# Parameters
num_snakes = 5
num_ladders = 5

# Setting min and max positions for snake heads and tails, and ladder bases and tops.
min_snake_head = 2 # The shortest and lowest snake could possibly be from 2 to 1.
max_snake_head = 100 # Not inclusive. Last square is where a player wins.

min_snake_tail = 1 # Inclusive.

max_ladder_base = 100 # Exclusive. Can't have a ladder base on the last square.
min_ladder_base = 2 # Inclusive. We decided to keep the first square clean of ladders.

max_ladder_top = max_ladder_base + 1 # Exclusive. 
min_ladder_top = min_ladder_base + 1 # Inclusive. 


# Task1 procedure

# Player 1 Name
p1_name = "Red"

# Player 1 Position
p1_position = 0

# Player 2 Name
p2_name = "Blue"

# Player 2 Position
p2_position = 0

# Snake Head Positions
# ~~~~~~~~~~~~~~~~~~~~
# We are choosing integers randomly from a range.
snake_heads = choices(range(min_snake_head, max_snake_head), k=num_snakes)

# Snake Tail Positions
# ~~~~~~~~~~~~~~~~~~~~
# 1. Now you have 5 snake heads locations
# 2. That means that the available location for tails is a list of 1 to 99, 
#    excluding snake_heads
# 3. We create a new list using a similar method to step 2.
# 4. Iterate 5 times, where each element has to be lower than its 
#    corresponding element in snake_heads.
# 5. Update the list of "non-available squars" so each snake will have its own
#    unique square for a tail.

snake_tails = []
for snake_head in snake_heads:
    snake_tails.append(choice(list(set(list(range(min_snake_tail, snake_head))) - set(snake_heads + snake_tails))))

# Ladder Base Positions
# ~~~~~~~~~~~~~~~~~~~~~
# First, create a list that combines snake_heads and snake_tails. We will Use
# this list to exclude its elements from the entire board, in order to pick
# unique positions for the ladders.

snake_positions = snake_heads + snake_tails

# Repeat the process we used to find snake_tails and adjust it, so we will
# determine ladder bases.

ladder_bases = []
for ladder_base in range(num_ladders):
    ladder_bases.append(choice(list(set(list(range(min_ladder_base, max_ladder_base))) - set(snake_positions + ladder_bases))))

# Ladder Tops Positions
# ~~~~~~~~~~~~~~~~~~~~~
# We repeat the same process again for ladder tops.

already_taken = snake_positions + ladder_bases
ladder_tops = []
for ladder_base in ladder_bases:
    ladder_tops.append(choice(list(set(list(range(ladder_base, max_ladder_top))) - set(already_taken + ladder_tops))))


# Print the position for Player 1
print(f"Player 1 position is: {p1_position}")
# Print the position for Player 2
print(f"Player 2 position is: {p2_position}")

# Task 2 begins here 
# Roll the dice for the first player
diceroll = roll_the_dice()

# Write the logic to move the first player
p1_position += diceroll

# Roll the dice for the second player
diceroll = roll_the_dice()

# Write the logic to move the second player
p2_position += diceroll

# Print the position for Player 1
print(f"Player 1 position is: {p1_position}")
# Print the position for Player 2
print(f"Player 2 position is: {p2_position}")

pre_alter = snake_heads + ladder_bases
post_alter = snake_tails + ladder_tops

# Check if player 1 is either on a snake head or ladder Base

# Check if player 2 is either on a snake head or ladder Base

# Update the positions if required

if p1_position in pre_alter:
    p1_position = post_alter[pre_alter.index(p1_position)]

if p2_position in pre_alter:
    p2_position = post_alter[pre_alter.index(p2_position)]

# Print the position for Player 1
print(f"Player 1 position is: {p1_position}")

# Print the position for Player 2
print(f"Player 2 position is: {p2_position}")
