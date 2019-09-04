#Regex Pipes and Groups

import re

message ="My number is 775-737-8248"
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #Pass in regular Expression
#Seperate groups with ()
matchObject = phoneNumRegex.search(message)
print(matchObject.group())

areaCode = matchObject.group(1)
phoneNumber = matchObject.group(2)

print(areaCode)
print(phoneNumber)

batMessage = "batman drive the batmobile from the batcoptor batbat"
batRegex = re.compile(r'bat(man|mobile|coptor|bat)')
batMatchObject = batRegex.search(batMessage)
batMatchObjectFindAll = batRegex.findall(batMessage)
print(batMatchObject.group())
print(batMatchObjectFindAll)
