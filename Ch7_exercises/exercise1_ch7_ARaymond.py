######################################
# Creator: Alfio Raymond
# Date: 9 Feb 2023
#
# Exercise 1 in Chapter 7
# Write a program to read through a file and print the contents of the file 
# (line by line) all in upper case. Executing the program will look as follows:
# python shout.py
# Enter a file name: mbox-short.txt
# FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
# RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
# RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
#     BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
#    SAT, 05 JAN 2008 09:14:16 -0500
#
# N/A
######################################

def main():
    fname = input('Enter the file name: ')
    try:
        fhand = open(fname)
    except:
        print("File cannot be opened: ", fname)
        exit()
    for line in fhand:
        print(line.upper())
    
main()