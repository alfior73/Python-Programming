######################################
# Creator: Alfio Raymond
# Date: 7 Feb 2023
#
# Exercise 4 in Chapter 6
# There is a string method called count that is similar to the function in the 
# previous exercise.
# Write an invocation that counts the number of times the letter a occurs in “banana”.
#
# N/A
######################################


def count(strInput, letterInput):
    word = strInput 
    
    count = strInput.count(letterInput)
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