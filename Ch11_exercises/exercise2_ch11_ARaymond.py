######################################
# Creator: Alfio Raymond
# Date: 20 March 2023
#
# Problem Set 7
# Write a program to look for lines of the form:
# New Revision: 39772
# Extract the number from each of the lines using a regular expression and the findall() method. 
# Compute the average of the numbers and print out the average as an integer.
# Enter file: mbox.txt
# 38549
# Enter file: mbox-short.txt
# 39756
#
#####################################

import re
import math

filename = input("Enter a file: ")

if len(filename) < 1:
    filename = 'Ch7_exercises/mbox-short.txt'

try:
    fhand = open(filename)
except:
    fhand = ''
    print('File cannot be opened', fhand)
    exit()

numbers = []

for line in fhand:
    match = re.search("New\sRevision:\s(\d+)", line)
    if match:
        numbers.append(int(match.group(1)))

print(math.floor(sum(numbers)/len(numbers)))


