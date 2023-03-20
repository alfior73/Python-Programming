######################################
# Creator: Alfio Raymond
# Date: 9 March 2023
#
# Exercise 6 in Chapter 8
# Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at
# the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use the max() 
# and min() functions to compute the maximum and minimum numbers after the loop completes.
# Enter a number: 6
# Enter a number: 2
# Enter a number: 9
# Enter a number: 3
# Enter a number: 5
# Enter a number: done
# Maximum: 9.0
# Minimum: 2.0
#
# N/A
######################################

def main():

    values = []

    while True:
        inputValue = input("Enter a value:")

        if inputValue == 'done': break

        try:
            value = float(inputValue)

        except:
            print("Numerical values only!")
            continue
        values.append(value)

    print("\nMinimum: ", min(values))
    print("Maximum: ", max(values))


main()
