mailFile = open("mbox.txt", "r")
contacts = open("myContacts.txt", "w")

for line in mailFile:
    lowerLine = line.lower()
    if lowerLine.startswith("from:"):
         st = line.find(":")
         fromUser = line[st+1:].strip()
         contacts.write(f"{fromUser}\n")

contacts.close()
mailFile.close()
