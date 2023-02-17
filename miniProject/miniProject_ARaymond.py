######################################
# Creator: Alfio Raymond
# Date: 5 Feb 2023
# 00142356
# CIS-153-O1A
#
#
# MINI PROJECT
# 
# See ReadMe_miniProject_ARaymond.txt
#
#########################################

import random

def fortuneTeller():
    while True:
        userInput = input("""What would you like to know from Madam Curiosity?
(Ask me a question - To exit type 'done'): """)
        if userInput == 'done':
            break
       
        randNumber = random.randint(1, 6)
        
        if randNumber == 1:
            result = 'Yes'
        elif randNumber == 2:
            result = 'No'
        elif randNumber == 3:
            result = 'Maybe'
        elif randNumber == 4:
            result = 'Try Again Later'
        elif randNumber == 5:
            result = 'No Chance'
        else:
            result = 'Absolutely'
        
        print("\n", userInput, result, "\n")
    
def banana():
    print("Banana")
    
def notWorking():
    print("That's not how this works")
    
def knockKnock():
    counter = 3
    while True:
        if counter != 0:
            userInput1 = input("Knock Knock ")
        
            if userInput1 == 'done':
                break
            
            if userInput1 == "Who's there" or userInput1 == "Who is there":
                banana()
                
                userInput2 = input("\n")
                
                if userInput2 == "Banana who" or userInput2 == "banana who":
                    counter = counter - 1
                else:
                    notWorking()                    
            else:
                notWorking()
            continue
        else:
            userInput3 = input("Knock Knock ")
            
            if userInput3 == "Who's there" or userInput3 == "Who is there":
                print("Orange")
                userInput4 = input("\n")
                if userInput4 == "Orange who" or userInput4 == "orange who":
                    print("Orange you glad I didn't say banana")
                    break
                else:
                    notWorking()    
            else:
                notWorking()
            
            
    
def MadLibs(nounFunc, verbFunc, adjFunc):
    
    randNumber = random.randint(1, 4)
    if randNumber == 1:
        madLibsFinale = "\nThere was a(n) " + adjFunc + " " + nounFunc + " that spent the day " + verbFunc + " his friends.\n"
    elif randNumber == 2:
        madLibsFinale = "\nIt's me G. Washington. I am concerned by the " + adjFunc + " state of affairs in America these days. It seems that your politicians are more concerned with " + verbFunc + " one another than with listening to the " + nounFunc + " of the people.\n"
    elif randNumber == 3: 
        madLibsFinale = "\nMy name is " + nounFunc + ". If I were president, I'd do a whole bunch of " + adjFunc + " things. I would live in the Statue of " + nounFunc + " and build a " + verbFunc + " pool at her feet.\n"
    else:
        madLibsFinale = "\nYoda says '" + verbFunc + " " + nounFunc + " " + adjFunc + "'\n"
    return madLibsFinale
    
    
def main():
    print("\nWelcome to Bozo's curiosity corner!")
    
    while True:
        print(" 1-Fortune Teller | 2-Knock Knock | 3-Mad Libs | 4-Exit")
        mainQuestion = input("Pick an option:")
       
        try:
            mainQuestion = int(mainQuestion)
            if mainQuestion == 1:
                fortuneTeller()
            elif mainQuestion == 2:
                knockKnock()
            elif mainQuestion == 3:
                print("Mad Mad Libs...so Mad it's cray cray")
                noun = input("Enter a noun: ")
                verb = input("Enter a verb: ")
                adjective = input("Enter an adjective: ")
                madlibOutput = MadLibs(noun, verb, adjective)
                print(str(madlibOutput))
            else:
                print("See ya wouldn't want to be ya!")
                break
        except:
            print("Must be a numeric value! ")
            
main()
