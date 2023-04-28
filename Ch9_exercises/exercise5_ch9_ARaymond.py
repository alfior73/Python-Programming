######################################
# Creator: Alfio Raymond
# Date: 3 March 2023
#
# Exercise 5 in Chapter 9
# This program records the domain name (instead of the address) where the 
# message was sent from instead of who the mail came from (i.e., the whole email address). 
# At the end of the program, print out the contents of your dictionary.
# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7, 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
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

domains = dict()

for line in fhand:
    if line.startswith("From "):
        counts = line.split()[1]
        domain = counts.split('@')[1]

        domains[domain] = domains.get(domain, 0) + 1

print(domains)
