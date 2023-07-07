import re

filename = input("Enter a file: ")
if len(filename) < 1:
    filename = 'miniProject3/access_log.txt'

try:
    fhand = open(filename)
except:
    fhand = ''
    print('File cannot be opened', fhand)
    exit()

links = dict()
lst = []
lstIPLink = []
for line in fhand:
    lst = line.split()
    link = lst[6]
    client = lst[0]
    lstIPLink = link, client
    
    links[lstIPLink] = links.get(lstIPLink, 0) + 1


max_hits = 0
max_link = None

for k in links:
    if links[k] > max_hits:
        max_link = k
        max_hits = links[k]
   
print(max_hits, max_link)


    
    
    # link = lstIP.split('?')
    # baseLink = link[0]
    # links[baseLink] = links.get(baseLink, 0) + 1

    # lst = []
    # for k, v in links.items():
    #     lst.append((v, k))

    # lst.sort(reverse=True)

    # requestor_tup = lst[0]

    # ipAddress = line.find(lst[0][1])
    # print(ipAddress)
    # print(lst)
    
    