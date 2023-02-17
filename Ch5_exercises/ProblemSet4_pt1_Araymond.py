######################################
# Creator: Alfio Raymond
# Date: 13 Feb 2023
#
# Problem Set 4 Part 1
# Write a program that meets the following specifications:
#
#    
# 1. define a function called validated_age, that takes no parameters and returns an integer. 
#    The function will prompt the user for their age and test that the age is greater than 0 and less than 150. 
#    If the age is invalid, the function should use a loop to print an error message and asking for an age, 
#    this will repeat unitl a valid age is provided. Once a valid age is entered it should be returned
# 2. define a function called main that prints a welcome message to the user and then calls the validate age function. 
#    Store the return value in a variable and print the result.
# 3. call main
#
#####################################
def validated_age():
    ageVerified = 0
    returnValue = 0
    while True:
        ageVerifier = input("What is your age(Type 'done' to exit): ")

        if ageVerifier == 'done':
            quit()

        ageVerifier = int(ageVerifier)
        #print("Age Verifier: ", ageVerifier)
        if ageVerifier > 0 and ageVerifier < 150:
            returnValue = ageVerifier
        else:
            print("Error, Enter a valid age!")
            continue

        return returnValue    
        
    
def main():
    
    print("----- Welcome to age verification -----")
    ageValidated = validated_age()
    print("Age Validated:", ageValidated)
        
main()
        