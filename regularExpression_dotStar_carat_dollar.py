import re

beginsWithHelloRegex = re.compile(r'^Hello')
#has to begin with hello

endsWithWorldRegex = re.compile(r'world!$')
#must end with world at the end of the string

digitMessage = "12345456546646"
allDigitRegex = re.compile(r'^\d+$')
digitObject = allDigitRegex.search(digitMessage)
digitGroup = digitObject.group()
#must have all digits
print(digitGroup)

Message = "First name: Mir Last Name: Hossain"
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
nameRegexFindAll = nameRegex.findall(Message)
print(nameRegexFindAll)

serve = "<To serve humans> for dinner.>"
nonGreedy = re.compile(r'<(.*?)>')
print(nonGreedy.findall(serve))

greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))

#DOTALL matches everything including new lines
#CaSe Insenitive = re.IGNORECASE
