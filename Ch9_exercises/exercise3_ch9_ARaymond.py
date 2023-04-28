######################################
# Creator: Alfio Raymond
# Date: 3 March 2023
#
# Exercise 3 in Chapter 9
# Write a program to read through a mail log,
# build a his - togram using a dictionary to count
# how many messages have come from each email address, and print the dictionary.
# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}
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

emails = dict()

for line in fhand:
    if line.startswith("From "):
        counts = line.split()[1]
        emails[counts] = emails.get(counts, 0) + 1

print(emails)
