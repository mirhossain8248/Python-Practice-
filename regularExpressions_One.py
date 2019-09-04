#Regular Expression Basics
#775-737-8248
#find a phone number without regex

import re #Regex Library

def incorrectPrint():
    print('Not a valid phone number')

def findPhoneNumber(message):
    foundNumber=False

    for i in range(len(message)):
        chunk = message[i:i+12]
        if isPhoneNumber(chunk):
            print("Phone Number Found: " + chunk)
            foundNumber = True
    if foundNumber == False:
        print("No phone number found")

def isPhoneNumber(text): #function declaration
    phoneNumberLength = 12

    if len(text) != phoneNumberLength:
        return False
    #incorrectPrint()

    for i in range(0,3):
         if not text[i].isdecimal():
            return False #No Area Code
    #incorrectPrint()

    if text[3] != '-':
        return False # Missing the Dash
    #incorrectPrint()

    for i in range(4,7):
         if not text[i].isdecimal():
            return False #Next set
    #incorrectPrint()

    if text[7] != '-':
        return False # Missing the Dash
    #incorrectPrint()

    for i in range(8,12):
         if not text[i].isdecimal():
            return False #Next set
    #incorrectPrint()

    return True

print(isPhoneNumber('775-737-8248'))
message = 'Call me tomorrow at 775-737-8248'
messageTwo = 'Call me tomorrow at 775-737-8248 or 775-824-9921'
#findPhoneNumber(message)

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #Set up regex to find phone number
matchObject = phoneNumRegex.search(message) #search the string
matchObjectFindAll = phoneNumRegex.findall(messageTwo) #search the string
print(matchObject.group()) #print out the string,
print(matchObjectFindAll) #print out the string, dont use group for findall
