######################################
# Creator: Alfio Raymond
# Date: 18 Feb 2023
#
# Exercise 2 in Chapter 8
# Figure out which line of the program is still not properly guarded.
# See if you can construct a text file which causes the program to fail
# and then modify the program so that the line is properly guarded and
# test it to make sure it handles your new text file.
#
# N/A
######################################

def main():

    fhand = open('../Ch7_exercises/mbox-short.txt')
    count = 0

    for line in fhand:
        words = line.split()

        if len(words) == 0:
            continue
        if words[0] != 'From':
            continue
       
        print(words[2])


main()
