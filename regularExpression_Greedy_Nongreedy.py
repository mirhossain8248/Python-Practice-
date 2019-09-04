#Specific number of repetions
#When we add the question mark to a regex Expression
#What happens is that the group before the question mark
#can appear once or not at all

# * = 0 or more times

# + = 1 or more times
import re

message = "The adventures of batwoman"
batRegex = re.compile(r'bat(wo)?man')
matchObject = batRegex.search(message)
groupedObject = matchObject.group()
print(groupedObject)

phoneMessage = "Call me tomorrow at 737-8248"
phoneRegex = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)') #This makes it so we dont need an area code
matchObjectPhone = phoneRegex.search(phoneMessage)
groupedObjectPhone = matchObjectPhone.group()
print(groupedObjectPhone)


#Specific num of repetions
haMessage =  "hahahahahahah"
haRegex = re.compile(r'(ha){3}') #look for ha 3 times
matchObjectHa = haRegex.search(haMessage)
groupObjectHa = matchObjectHa.group()
print(groupObjectHa)

#If we wanted a range of repetions then we would have an upper and lower bound
#Ex: {3,5} 3-5 repetions would return a true statement

digitMessage = '3215873'
digitRegex = re.compile(r'(\d){3,5}')
#by nature the bounds are going to be greedy so its going to default to the
#upper bound if possible. If we wanted to stick to the lower bound then we
#would add a question mark after the {3,5}
matchObjectDigit = digitRegex.search(digitMessage)
groupObjectDigit = matchObjectDigit.group()
print(groupObjectDigit)
