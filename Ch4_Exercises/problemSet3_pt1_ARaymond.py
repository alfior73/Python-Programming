######################################
# Creator: Alfio Raymond
# Date: 5 Feb 2023
#
# Problem Set 3 Part 1
# Write a program that meets the following specifications:
#
#    Define a function called print_greeting. The function has one parameter, a name. 
#       When the funciton runs it prints "greetings" and the user's name
#    Define a function with a descriptive name that takes one parameter, an age, and returns True if
#       the user is at least 18 years old and false otherwise.
#    Define a function called "main" that creates 2 appropriately named variables, 
#       one for a username and one for an age. This function prompts the user for 
#       the information, uses input to store the values provided into the variables you created. 
#       Use the name varble to call the print_greeting function. Then use the age to call the 
#       age function you created. Store the results of the function call in a variable 
#       named is_age_valid. If is_age_valid is true, print "valid age" otherwise print "invalid age"
#   Do not use any global variables
#
#####################################
def printGreeting(name):
    print("Greetings", name)

def ageTester(age):
    ageTest = "None"
    if age >= '18':
        ageTest = "valid age"
    else:
        ageTest = "invalid age"
    return ageTest
        
    
def main():
    username = "None"
    age = "None"
    is_age_valid = "None"
    username = input("Enter your name: ")
    age = input("Enter your age: ")
    
    printGreeting(username)
    is_age_valid = ageTester(age)
    print(is_age_valid)
        
main()
