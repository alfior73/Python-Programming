######################################
# Creator: Alfio Raymond
# Date: 18 Feb 2023
#
# Exercise 3 in Chapter 8
# Rewrite the guardian code in the above example without two if statements.
# Instead, use a compound logical expression using the or logical operator
# with a single if statement.
#
# N/A
######################################

def main():

    fhand = open('../Ch7_exercises/mbox-short.txt')
    count = 0

    for line in fhand:
        words = line.split()

        if len(words) == 0 or words[0] != 'From':
            continue

        print(words[2])


main()
