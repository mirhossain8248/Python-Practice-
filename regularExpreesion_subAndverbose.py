import re

message = "Agent alice gave secret documents to Agent bob"
namesRegex = re.compile(r'Agent \w+')
namesFindAll = namesRegex.findall(message)
print(namesFindAll)

#find and replace
redactedMessage = namesRegex.sub("REDACTED" , message)
#Replace is the first argument, the message is the second
print(redactedMessage)

#Just have the initial of the Agent

newNamesRegex = re.compile(r'Agent (\w) \w+') #look for one word charecter
newNamesFindAll = newNamesRegex.findall(message)
newRedactedMessage = newNamesRegex.sub(r'Agent \1****' , message)
print(newRedactedMessage)

#Verbose mode

phoneNumRegex = re.compile(r'''
(\d\d\d)- #comment
(\d\d\d-
\d\d\d\d)''' , re.VERBOSE | re.IGNORECASE) #we can use OR to have multiple arguments

#Verbose makes it so the RE ignores whitespace and comments
