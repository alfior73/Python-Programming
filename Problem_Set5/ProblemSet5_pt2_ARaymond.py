######################################
# Creator: Alfio Raymond
# Date: 16 Feb 2023
#
# Problem Set 5 Part 2
# Write a function that takes 2 strings as paramters.
# The function should create a new string by appending the second stroing to the first.
# The new string should be returned by the function.
# Write a main program to test the function.
# Example: if the passed strings are "hello" and "world" the result should be "worldhello"
#
#####################################

def switcheroo(word1, word2):
    switcherooWord = word2+word1
    return switcherooWord


def main():
    userInput1 = input("Enter your first word:")
    userInput2 = input("Enter your second word:")

    funcReturn = switcheroo(userInput1, userInput2)

    print(funcReturn)


main()
