######################################
# Creator: Alfio Raymond
# Date: 7 Feb 2023
#
# Exercise 2 in Chapter 6
# Given that fruit is a string, what does fruit[:] mean?
# Fruit[:] will print out the full string
#
# N/A
######################################

def main():
    
    while True:
        strInput = input("Enter a word to parse(type 'done' to exit): ")
        
        if strInput == 'done':
            break
        elif strInput == '':
            continue
            
        print(strInput[:])
    
    
main()