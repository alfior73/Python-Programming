######################################
# Creator: Alfio Raymond
# Date: 20 March 2023
#
# Problem Set 7 
# Revise a previous program as follows: 
# Read and parse the “From” lines and pull out the addresses from the line. 
# Count the num- ber of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating a list of(count, email) tuples from the dictionary. 
# Then sort the list in reverse order and print out the person who has the most commits.
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09: 14: 16 2008
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195
#
#####################################

filename = input("Enter a file: ")
if len(filename) < 1:
    filename = 'Ch7_exercises/mbox-short.txt'

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

lst = []
for key, value in emails.items():
    lst.append((value, key))

lst.sort(reverse = True)

person_tup = lst[0]

print(person_tup[1], person_tup[0])
