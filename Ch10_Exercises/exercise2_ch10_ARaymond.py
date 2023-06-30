######################################
# Creator: Alfio Raymond
# Date: 20 March 2023
#
# Problem Set 7
# This program counts the distribution of the hour of the day for each of the messages. 
# You can pull the hour from the “From” line by finding the time string and then splitting
# that string into parts using the colon character. 
# Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.
# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1
#
#####################################

filename = input("Enter a file: ")
if len(filename) < 1:
    fhand = 'Ch7_exercises/mbox-short.txt'

try:
    fhand = open(fhand)
except:
    fhand = ''
    print('File cannot be opened', fhand)
    exit()

hourly = dict()

for line in fhand:
    if line.startswith("From "):
        time = line.split()[5]
        hour = time.split(':')[0]
        hourly[hour] = hourly.get(hour, 0) + 1

lst = list(hourly.items())
lst.sort()

for i in lst:
    print(i[0], i[1])

