######################################
# Creator: Alfio Raymond
# Date: 3 March 2023
#
# Exercise 4 in Chapter 9
# Add code to the above program to figure out who has the most messages in the file.
# After all the data has been read and the dic- tionary has been created, 
# look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops)
# to find who has the most messages and print how many messages the person has.
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195
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

largest = -1
email = None

for k, v in emails.items():
    if v > largest:
        largest = v
        email = k

print(email,largest)

