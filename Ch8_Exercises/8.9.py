s = 'spam'
t = list(s)
print(t)

s = "pining for the fjords"
t = s.split()
print(t)
print(t[2])

s = 'spam-spam-spam'
delimiter = '-'
# outputs ['spam', 'spam', 'spam']
s.split(delimiter)

t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
# outputs 'pining for the fjords'
delimiter.join(t)