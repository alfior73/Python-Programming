######################################
# Creator: Alfio Raymond
# Date: 20 March 2023
#
# Problem Set 7
# Write a simple program to simulate the operation of the grep command on Unix.
# Ask the user to enter a regular expression and count the number of lines that matched the regular expression:
# $ python grep.py
# Enter a regular expression: ^ Author
# mbox.txt had 1798 lines that matched ^ Author
# $ python grep.py
# Enter a regular expression: ^ X-
# mbox.txt had 14368 lines that matched ^ X-
# $ python grep.py
# Enter a regular expression: java$
# mbox.txt had 4175 lines that matched java$
#
#####################################

import re

filename = input("Enter a file: ")
regExpression = input("Enter a regular expression: ")

if len(filename) < 1:
    filename = 'Ch7_exercises/mbox-short.txt'

try:
    fhand = open(filename)
except:
    fhand = ''
    print('File cannot be opened', fhand)
    exit()

count = 0


for line in fhand:
    line = line.rstrip()
    if re.search(regExpression, line):
        count += 1

print(filename, "had", count, "lines that matched", regExpression)
