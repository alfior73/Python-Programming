######################################
# Creator: Alfio Raymond
# Date: 1 Feb 2023
#
# Exercise 2 in Chapter 5
# Write another program that prompts for a list of numbers as above 
# and at the end prints out both the maximum and minimum of the numbers
# instead of the average.
#
#
# N/A
######################################

def main():
    smallest = 1000000
    largest = -1
    inputValue = 0
    
    while True:
        inputValue = input("Enter a number: ")
        if inputValue == 'done':
            break
        try:
            inputValue = float(inputValue)
        except:
            print("Invalid Input")
            continue

        if inputValue < smallest:
            smallest = inputValue
        elif inputValue > largest:
            largest = inputValue
        
        
    print("Max Value: ", largest)
    print("Min Value: ", smallest)
    
    
main()