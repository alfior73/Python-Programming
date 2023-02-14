######################################
# Creator: Alfio Raymond
# Date: 9 Feb 2023
#
# Exercise 3 in Chapter 7
# Sometimes when programmers get bored or want to have a bit of fun, 
# they add a harmless Easter Egg to their program. Modify the program that prompts 
# the user for the file name so that it prints a funny message when the user types 
# in the exact file name “na na boo boo”. The program should behave normally for 
# all other files which exist and don’t exist. Here is a sample execution of the program:
# python egg.py
# Enter the file name: mbox.txt
# There were 1797 subject lines in mbox.txt
# python egg.py
# Enter the file name: missing.tyxt
# File cannot be opened: missing.tyxt
# python egg.py
# Enter the file name: na na boo boo
# NA NA BOO BOO TO YOU - You have been punk'd!
#
# N/A
######################################

def main():
    count = 0
    avgConfidence = 0
    
    fname = input('Enter the file name: ')
    
    if fname == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        quit()
    else:    
        try:
            fhand = open(fname)
        except:
            print("File cannot be opened: ", fname)
            exit()

        for line in fhand:
            if line.startswith('X-DSPAM-Confidence:'):
                index = line.find(' ')
                number = float(line[index+1:])
                avgConfidence += number
                count = count + 1

        print('Average spam confidence:', avgConfidence/count)

        

    
            
main()