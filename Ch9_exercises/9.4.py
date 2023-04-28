import string
string.punctuation 
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

fname = 'Ch8_Exercises/romeo-full.txt'

try:
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    exit()

counts=dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)
