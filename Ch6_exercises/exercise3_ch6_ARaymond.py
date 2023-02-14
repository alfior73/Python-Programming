######################################
# Creator: Alfio Raymond
# Date: 7 Feb 2023
#
# Exercise 3 in Chapter 6
# Encapsulate this code in a function named count, and generalize
# it so that it accepts the string and the letter as arguments.
#
# N/A
######################################


def count(strInput, letterInput):
    word = strInput 
    count = 0
    for letter in word:
        if letter == letterInput: 
            count = count + 1
    print(letterInput.capitalize() + "'s:",count)
    
def main():
    
    while True:
        strInput = input("Enter a string (Type 'done' to exit): ")
        
        if strInput == 'done':
            break
        elif strInput == '':
            continue
        else:
            letterInput = input("What letter should be found: ")
            count(strInput, letterInput)
            
main()