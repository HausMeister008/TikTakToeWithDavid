INFO PROJECT LEON DAVID
Objective:
Programm a certain game (you may choose it your self) and completely create a python script.

# __USAGE__
# Run Gameboard.py in a terminal like Visual Studio Code with
# python .\Gameboard.py
# this will include the player.py file.
# Firstly you'll have to choose your Field size
# 3X3
# | | 
# | |
# | |
# (filed)
# y|y|x
# y|x|y
# x|y|x
# 5X5
# | | | |  
# | | | |
# | | | |
# | | | |
# | | | |
# ONLY ENTER A SINGLE DIGET NOT A TUPLE, JUST 3 OR 5
# .
# .
# .
# Now the two players are being initialized and the first one has to choose their Name and corresponding Icon, for example
What is your name?
>David
Choose your icon and you shall stick with it for ever:
>X
# Now the second player is initialized
What is your name?
>Leon
Choose your icon and you shall stick with it for ever:
>O
# Then the actual game starts
# The first player, that has been initialized now inputs to numbers, seperated by a comma
David, in which spaces to you want to write your x?
>1,1

# the layout of the field is from the top left to the Bottom Right corner
# the first corner is 1,1
1,1|2,1|3,1
1,2|2,2|3,2
1,3|2,3|3,3
# an extended field follows the same rules
# then player 2 has to choose a spot
# overwriting a spot is impossible
# this process continues until either one has won or the field is filled up
# termination in VSC is done with ctrl c or strg c
