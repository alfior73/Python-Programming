######################################
# Creator: Alfio Raymond
# Date: 7 Feb 2023
#
# Exercise 1 in Chapter 6
# Write a while loop that starts at the last character in the string and works 
# its way backwards to the first character in the string, printing each letter 
# on a separate line, except backwards.
#
# N/A
######################################


def main():
    index = 0
    strInput = input("Enter a word to parse: ")
    index = len(strInput)

    while index <= len(strInput):
        if index == 0:
            break
        letter = strInput[index-1]
        index = index - 1
        print(letter)
        
main()
        