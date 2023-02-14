######################################
# Creator: Alfio Raymond
# Date: 25 Jan 2023
#
# Exercise 1 in Chapter 4
# Run the program on your system and see what numbers you get. 
# Run the program more than once and see what numbers you get.
# The random function is only one of many functions that handle random numbers. 
# The function randint takes the parameters low and high, and returns an integer 
# between low and high (including both).
# >>> random.randint(5, 10)
# 5
# >>> random.randint(5, 10)
# 9

# To choose an element from a sequence at random, you can use choice:
# >>> t = [1, 2, 3]
# >>> random.choice(t)
# 2
# >>> random.choice(t)
# 3
# The random module also provides functions to generate random values from continuous 
# distributions including Gaussian, exponential, gamma, and a few more.
#
# N/A
######################################

import random

randNumber = random.randint(5, 10)
print("Random Number: ", randNumber)

t = [1, 2, 3]
choiceNumber = random.choice(t)

print("Choice Number: ", choiceNumber)
