######################################
# Creator: Alfio Raymond
# Date: 3 March 2023
#
# Problem Set 6 Part 2
# Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with “From”,
# then look for the third word and keep a running count of each of the days of the week.
# At the end of the program print out the contents of your dictionary (order does not matter).
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09: 14: 16 2008
# Sample Execution:
# python dow.py
# Enter a file name: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}
#
#####################################

filename = input("Enter a file: ")
if len(filename) < 1:
    filename = 'Ch7_Exercises/mbox-short.txt'

try:
    fhand = open(filename)
except:
    fhand = ''
    print('File cannot be opened', fhand)
    exit()

days = dict()

for line in fhand:
    if line.startswith("From "):
        day = line.split()[2]
        days[day] = days.get(day, 0) + 1
        
print(days)

