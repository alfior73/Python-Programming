######################################
# Creator: Alfio Raymond
# Date: 17 Feb 2023
#
# Exercise 1 in Chapter 8
# Write a function called chop that takes a list and modifies it, 
# removing the first and last elements, and returns None. 
# Then write a function called middle that takes a list and 
# returns a new list that contains all but the first and last elements.
#
# N/A
######################################

def chop(letters):
    chopResult = 'None'

    del letters[0]
    del letters[4]

    return chopResult


def middle(letters):
    middleResult = 'none'
    middleResult = letters
    return middleResult


def main():

    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    result = chop(letters)
    print('Result:', result)
    result2 = middle(letters)
    print('Result2:', result2)


main()
