######################################
# Creator: Alfio Raymond
# Date: 16 Feb 2023
#
# Problem Set 5 Part 3
# Write a function that takes a string and a character to target as input.
# The function should return the number of times the character shows up in the string regardless of case.
# Write a main program to test the function.
# Example: functions gets the string "GOOD show" and the letter o, the result should be 3
#
#####################################

def functionFind(word, character):

    count = 0

    for letter in word:
        if letter == character:
            count = count + 1

    result = count
    return result


def main():

    userInput1 = input("Enter a string/word/sentance:")
    userInput2 = input("Enter a character:")

    funcResult = functionFind(userInput1, userInput2)

    print(userInput2.capitalize() + "'s found: ", funcResult)


main()
