#This program will scrape the phone numbers and emails from a pdf

#TO DO: create a regex for phone numbers
#regex for email addresses
#get text from clipboard
#extract email/phone from text

import re, pyperclip
#Regex for phone numbers

#types of phone numbers
#775-737-8248, 777-8248, (775) 737-8248, ext 12345, ext. 12345 x12345

phoneRegex = re.compile(r'''
#775-737-8248, 777-8248, (775) 737-8248, ext 12345, ext. 12345 x12345

(
((\d\d\d)|(\(\d\d\d\)))?    # area code (optional)
(\s|-)                      # first separator
\d\d\d                      # first 3 digits
-                           # separator
\d\d\d\d                    # last 4 digits
(((ext(\.)?\s)|x)           # extension word-part (optional)
(\d{2,5}))?                 # extension number-part (optional)
)

''', re.VERBOSE)

#Regex for emails
emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com

[a-zA-Z0-9_.+]+              # name part
@                            # @ symbol
[a-zA-Z0-9_.+]+              #domain name part

''', re.VERBOSE)

#Text from clipboard
text = pyperclip.paste()

#Extract emails/phones
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

#print(extractedPhone)
#print(extractedEmail)

#format results to be readable

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
