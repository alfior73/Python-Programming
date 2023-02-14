######################################
# Creator: Alfio Raymond
# Date: 13 Feb 2023
#
# Problem Set 4 Part 2
# Write a program that uses a while loop to keep track of the sum of even numbers. 
# The loop will take inpurt from the user. A total of the positive even numbers is kept,
# the loop should ignore positive odd numbers, and negative numbers will end the loop
#   1. prompt the user for a number
#   2. if the number is negatie, use a break to leave the loop
#   3. if the number is a positive odd, use a continue to skip the rest of the loop but continue the iteration
#   4. if the number is postive even number add this to an accumulator variable
#
#
#####################################
    
def main():
    totalValue = 0
    inputValue = 0
    evalValue = 0
    
    print("****** Positive Number Taker ******")
    while True:
        inputValue = input("Enter a value:")
        
        try:
            inputValue = float(inputValue)
        
            if inputValue < 0:
                break
        
            evalValue = inputValue % 2
            
            if evalValue == 0:
                totalValue += inputValue
            else:
                continue
        except:
            print("Numerical values only!")
            continue
            
    print("Total value:",totalValue)    
        
main()


        
     


        