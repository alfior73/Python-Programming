Alfio Raymond
CIS-153-O1A
10 March 2023

Assignments
-----------
Problem Set 6


Description
-----------
Exercise 4 in Chapter 8
     Find all unique words in a file Shakespeare used over 20, 000 words in his works. 
     But how would you determine that? How would you produce the list of all the words 
     that Shakespeare used? Would you download all his work, read it and track all unique words by hand?
     Let’s use Python to achieve that instead. List all unique words, sorted in alphabetical order, 
     that are stored in a file romeo.txt containing a subset of Shakespeare’s work.
     To get started, download a copy of the file www.py4e.com/code3/romeo.txt. 
     Create a list of unique words, which will contain the final result. Write
     a program to open the file romeo.txt and read it line by line. For each
     line, split the line into a list of words using the split function. 
     For each word, check to see if the word is already in the list of unique words. 
     If the word is not in the list of unique words, add it to the list.
      When the program completes, sort and print the list of unique words in alphabetical order.
         Enter file: romeo.txt
         ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief',
             'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window',
                'with', 'yonder']

Exercise 5 in Chapter 8
     Write a program to read through the mail box data and when you find line that starts with “From”,
     you will split the line into words using the split function. We are interested in who sent the message,
     which is the second word on the From line.
         From stephen.marquard@uct.ac.za Sat Jan 5 09: 14: 16 2008
    You will parse the From line and print out the second word for each From line,
    then you will also count the number of From (not From:) lines and print out a count at the end.
    This is a good sample output with a few lines removed:
        python fromcount.py
        Enter a file name: mbox-short.txt
        stephen.marquard@uct.ac.za
        louis@media.berkeley.edu
        zqian@umich.edu
        [...some output removed...]
        ray@media.berkeley.edu
        cwen@iupui.edu
        cwen@iupui.edu
        cwen@iupui.edu
        There were 27 lines in the file with From as the first word


Exercise 6 in Chapter 8
    Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at
    the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use the max() 
    and min() functions to compute the maximum and minimum numbers after the loop completes.
    Enter a number: 6
    Enter a number: 2
    Enter a number: 9
    Enter a number: 3
    Enter a number: 5
    Enter a number: done
    Maximum: 9.0
    Minimum: 2.0

Exercise 3 in Chapter 9
    Write a program to read through a mail log, 
    build a his - togram using a dictionary to count 
    how many messages have come from each email address, and print the dictionary.
    Enter file name: mbox-short.txt
    {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
    'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
    'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
    'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
    'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
    'ray@media.berkeley.edu': 1}

Exercise 4 in Chapter 9
    Add code to the above program to figure out who has the most messages in the file.
    After all the data has been read and the dic- tionary has been created, 
    look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops)
    to find who has the most messages and print how many messages the person has.
    Enter a file name: mbox-short.txt
        cwen@iupui.edu 5
    Enter a file name: mbox.txt
        zqian@umich.edu 195

Exercise 5 in Chapter 9 
    This program records the domain name (instead of the address) where the 
    message was sent from instead of who the mail came from (i.e., the whole email address). 
    At the end of the program, print out the contents of your dictionary.
    python schoolcount.py
    Enter a file name: mbox-short.txt
        {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7, 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}


Instructions
------------
All programs run with a simple python command 
Depending on the program/script it'll ask for input or not. I even included a catchall where if you don't specify the file, it'll grab a default file
in the code.
You can do as the examples states up above or in the comment header. 

For the Chapter 8 exercises they should be stored in the subfolder titled "Ch8_Exercises" with the specified txt files.
For the Chapter 9 exercises they should be stored in the subfolder titled "Ch9_exercises" with the specified txt files.



Completion Statement
--------------------
I was able to complete most parts of the assignment by myself. 