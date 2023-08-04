######################################
# Creator: Alfio Raymond
# Date: 22 Feb 2023
# 00142356
# CIS-153-O1A
#
#
# MINI PROJECT 2
#
# See ReadMe_miniProject2_ARaymond.txt
#
#########################################
import random
from datetime import datetime


def setUsernameFunc():
    while True:
        userFirstNameInput = input("Enter your First Name:")
        userLastNameInput = input("Enter you Last Name:")

        if userFirstNameInput.find(':') > 0 or userLastNameInput.find(':') > 0:

            userFirstNameInput = userFirstNameInput.replace(':', '')
            userLastNameInput = userLastNameInput.replace(':', '')
            getUserNameResult = CreateUserNameFunc(
                userFirstNameInput, userLastNameInput)

        else:
            getUserNameResult = CreateUserNameFunc(
                userFirstNameInput, userLastNameInput)

        return getUserNameResult
#### End of setUsername Function ########################################################


def CreateUserNameFunc(firstNameInput, lastNameInput):

    randNumber = random.randint(1000, 9999)

    createUserNameResult = firstNameInput[0] + lastNameInput + str(randNumber)

    return createUserNameResult
#### End of CreateUserName Function ########################################################


def encryptPasswordFunc(userPasswordInput):
    # print(userPasswordInput)
    userPasswordFirst = userPasswordInput[0]
    userPasswordLast = userPasswordInput[len(userPasswordInput) - 1]
    userPasswordMiddle = userPasswordInput[1:len(userPasswordInput)-1]

    userPasswordMiddle = userPasswordMiddle.replace('i', '!')
    userPasswordMiddle = userPasswordMiddle.replace('a', '@')
    userPasswordMiddle = userPasswordMiddle.replace('S', '$')
    userPasswordMiddle = userPasswordMiddle.replace('J', '?')

    userPasswordResult = userPasswordLast + userPasswordMiddle + userPasswordFirst

    return userPasswordResult
#### End of encriptPassword Function ########################################################


def ValidPasswordFunc(userPasswordInput):

    if userPasswordInput.find('!') > 0:
        print("You enter '!'; no special characters")
        newPasswordFunc()
    elif userPasswordInput.find('@') > 0:
        print("You enter '@'; no special characters")
        newPasswordFunc()
    elif userPasswordInput.find('$') > 0:
        print("You enter '$'; no special characters")
        newPasswordFunc()
    elif userPasswordInput.find(':') > 0:
        print("You entered ':'; no special characters")
        newPasswordFunc()
    elif userPasswordInput.find('?') > 0:
        print("You entered '?'; no special characters")
        newPasswordFunc()
    else:
        encryptPasswordResult = encryptPasswordFunc(userPasswordInput)

    return encryptPasswordResult
#### End of ValidPassword Function ########################################################


def newPasswordFunc():
    newPassword = ''
    while True:
        userPasswordEntry1 = input("Enter a password:")
        userPasswordEntry2 = input("Re-enter the password:")

        if userPasswordEntry1 != userPasswordEntry2:
            print("Passwords do not match")
            continue
        elif len(userPasswordEntry1) < 7 or len(userPasswordEntry2) < 7:
            print("Password is not long enough")
            continue
        else:
            newPassword = ValidPasswordFunc(userPasswordEntry1)
            break

    return newPassword
#### End of newPassword Function ########################################################


def addUserFunc(userName, password):
    addUser = ''
    addUserLogin = userName + ":" + password + "\n"
    addUserFileName = 'miniProject2/addUsers.txt'

    try:
        userFileOutput = open(addUserFileName)
        addUser = userFileOutput.read()
    except:
        userFileOutput = open(addUserFileName, 'w')

    if addUser == '':
        userFileOutput = open(addUserFileName, 'w')
        userFileOutput.write(addUserLogin)
    else:
        userFileOutput = open(addUserFileName, 'w')
        addUser = addUser + addUserLogin
        userFileOutput.write(addUser)

    userFileOutput.close()

    #### End of addUser Function ########################################################


def writeToLogFunc(username, user):
    addLog = ''
    local = datetime.now()
    newUserLogFileName = 'miniProject2/newUserLog.txt'

    if user == '1':
        status = "NEW USER"
    elif user == '2':
        status = "OK"
    elif user == '3':
        status = "BAD PASS"
    else:
        status = "BAD ACCOUNT"

    userWriteToLog = username + " : " + \
        str(local.strftime("%Y-%m-%d %H:%M")) + " : " + status + "\n"

    try:
        fhand = open(newUserLogFileName)
        addLog = fhand.read()
    except:
        fhand = open(newUserLogFileName, 'w')

    if addLog == '':
        fhand = open(newUserLogFileName, 'w')
        fhand.write(userWriteToLog)
    else:
        fhand = open(newUserLogFileName, 'w')
        addLog = addLog + userWriteToLog
        fhand.write(addLog)

    fhand.close()

    #### End of writeToLog Function ########################################################


def validateUserNameLogin():

    while True:
        userNameInput = input("Enter your Username:")

        if userNameInput.find(':') > 0:

            userNameInputReturn = userNameInput.replace(':', '')

        else:
            userNameInputReturn = userNameInput
            break

    return userNameInputReturn
#### End of getUsername Function ########################################################


def validatePasswordLogin():
    while True:
        passwordInput = input("Enter your Password:")

        if passwordInput.find('!') > 0:
            print("You enter '!'; no special characters")
            continue
        elif passwordInput.find('@') > 0:
            print("You enter '@'; no special characters")
            continue
        elif passwordInput.find('$') > 0:
            print("You enter '$'; no special characters")
            continue
        elif passwordInput.find(':') > 0:
            print("You entered ':'; no special characters")
            continue
        elif passwordInput.find('?') > 0:
            print("You entered '?'; no special characters")
            continue
        else:
            passwordInputReturn = encryptPasswordFunc(passwordInput)
            break

    return passwordInputReturn
#### End of getUsername Function ########################################################


def printLogFunc(username, printLog):
    printLog = 'y'
    logData = open('miniProject2/newUserLog.txt')

    if printLog == 'y':
        for line in logData:
            if line.startswith(username):
                print(line)

    logData.close()
#### End of printLog Function ########################################################


def checkUserFunc(username, password):
    checkUser = ''
    validAccount = 0
    local = datetime.now()
    checkUser = open('miniProject2/addUsers.txt')

    for line in checkUser:
        if line.startswith(username):
            data = line
            userData = data.find(':')
            endData = data.find('\n')
            usernameData = data[0:userData]
            passwordData = data[userData+1:endData]

            if usernameData == username:
                validAccount = 1
                if passwordData == password:
                    user = '2'
                    writeToLogFunc(username, user)
                    print("----------------------------------")
                    print("           Welcome back!          ")
                    print("----------------------------------")
                    printLog = input("Would you like to print the log(y/n)?")
                    if printLog == 'y':
                        printLogFunc(username, printLog)

                else:
                    user = '3'
                    writeToLogFunc(username, user)
                    print("----------------------------------")
                    print("       Incorrect Password         ")
                    print("----------------------------------")

    if int(validAccount) == 0:
        user = '4'
        writeToLogFunc(username, user)
        print("------------------------------------")
        print(" User not found - Create an Account ")
        print("------------------------------------")
#### End of checkUser Function ########################################################


def main():

    print("************ Welcome to Piggly Wiggly Banking ************")
    while True:
        print("1) Create Account 2) Login 3) Quit")
        user = input("Select option: ")

        if str(user) == '3':
            quit()
        elif str(user) != '1' and str(user) != '2':
            continue

        user = int(user)
        if int(user) == 1:
            getUserNameResult = setUsernameFunc()
            encryptPasswordResult = newPasswordFunc()
            print("Password is valid\n")

            addUserFunc(getUserNameResult, encryptPasswordResult)
            writeToLogFunc(getUserNameResult, str(user))
            print("-----------------------------------------------------")
            print("-        Login Info:", getUserNameResult)
            print("- Save your username & password for future use")
            print("-----------------------------------------------------\n")
        elif int(user) == 2:
            usernameInputReturn = validateUserNameLogin()
            passwordInputReturn = validatePasswordLogin()
            checkUserFunc(usernameInputReturn, passwordInputReturn)
            continue


main()
