#Word Count program

name = input('Enter file:')
handle = open(name, 'r')
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        

bigcount = None
bigword = None

for word, count in list(counts.items()):
    
        bigword = word
        bigcount = count

print(bigword, bigcount)