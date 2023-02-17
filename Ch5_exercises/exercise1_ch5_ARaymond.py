######################################
# Creator: Alfio Raymond
# Date: 31 Jan 2023
#
# Exercise 1 in Chapter 5
# Write a program which repeatedly reads numbers until the user enters “done”.
# Once “done” is entered, print out the total, count, and average of the numbers. 
# If the user enters anything other than a number, detect their mistake using try 
# and except and print an error message and skip to the next number.
#
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333
#
# N/A
######################################




def main():
    totalValue = 0
    countValue = 0
    inputValue = 0
    maxNumber = None
    minNumber = None
    
    while True:
        inputValue = input("Enter a number: ")
        if inputValue == 'done':
            break
        try:
            inputValue = float(inputValue)
        except:
            print("Invalid Input")
            continue

        countValue = countValue + 1
     

    print(totalValue,countValue,averageValue)
    
    
main()
