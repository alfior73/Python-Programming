import re
hand = open('Ch7_exercises/mbox-short.txt')

for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)
