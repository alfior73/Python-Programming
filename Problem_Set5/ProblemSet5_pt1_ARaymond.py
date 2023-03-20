######################################
# Creator: Alfio Raymond
# Date: 16 Feb 2023
#
# Problem Set 5 Part 1
# Write a program that prompts the user for their first name.
# Use the input to create a new string made first, middle, and last character of a users name.
# The middle is the string length divided by 2 using integer division.
# Example: if the user enter michael, the result would be mhl
#
#####################################

def main():
    userInput = input("Enter your first name:")

    firstSlice = userInput[0]
    lengthOfUserInput = len(userInput) // 2
    secondSlice = userInput[lengthOfUserInput]
    length = len(userInput)
    thirdSlice = userInput[length - 1]

    finalOutput = firstSlice+secondSlice+thirdSlice
    print(finalOutput.lower())


main()
