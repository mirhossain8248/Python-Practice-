#Charecter Classes, Findall
import re

message = "My phone numbers are: 775-737-8248, 775-824-9921"
phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
phoneObjectFindAll= phoneRegex.findall(message)
print(phoneObjectFindAll)

#Charecter classes are short cuts built in, we can just look them up

lyrics = '''4 calling birds
5 gold rings
6 geese a-laying
7 swans a-swimming
8 maids a-milking
9 ladies dancing 10 lords a-leaping 11 pipers piping 12 drummers drumming'''

xmasRegex = re.compile(r'\d+\s\w+') #looking for one or more digit, space, one or more letters
xmasObjectFindAll = xmasRegex.findall(lyrics)
print(xmasObjectFindAll)

#make your own char class (object):

vowelRegex = re.compile(r'[aeiouAEIOU]')
#can also use params (a-z) gets all lower letters
vowelObjectFindAll = vowelRegex.findall(lyrics)
print(vowelObjectFindAll)

#Negative Charecter class
#negativeVowelRegex = re.compile(r'[^aeiouAEIOU])
#negObjectFindAll = negativeVowelRegex.findall(lyrics)
#print(negObjectFindAll)
#
