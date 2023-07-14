######################################
# Creator: Alfio Raymond
# Date: 30 March 2023
#
# Problem Set 8
# Change your socket program so that it counts the number 
# of characters it has received and stops displaying any 
# text after it has shown 3000 characters. 
# The program should retrieve the entire document and count 
# the total number of characters and display the count of the 
# number of characters at the end of the document.
#
#####################################
import socket

try:
    webAddress = input("Enter Web Address:")
    host = webAddress.split('/')[2]

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))

    # data.pr4e.org/romeo.txt
    cmd = 'GET ' + webAddress + ' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()

    mysock.send(cmd)

    incomingData = b""
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        
    incomingData += data
    incomingData = incomingData.decode()
    print(incomingData[:3000])
    print(len(incomingData))

    mysock.close()
except:
    print("Please enter a properly formatted URL")
