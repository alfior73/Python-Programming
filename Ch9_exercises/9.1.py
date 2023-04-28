
word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = d.get(c,0) + 1
print(d)