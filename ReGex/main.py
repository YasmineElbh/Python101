#Example 1
import re
pattern = 'hello'
sequence = 'hello world'
if re.match(pattern, sequence):
    print('match!')
else:
    print('not a match!')

#Example 2
result = re.match(r'AV', 'AV Analytics vidhaya AV')
print(result.start())
print(result.end())

#Example3
r = re.match(r'AV', 'AV Analytics vidhaya AV')
print(r)

#Example4
#validate a phone number(phone nummber must be of 10 digits and starts with 8 or 9)

li = ['9999999999', '999999-99', '99999x999']
for val in li:
    if re.match(r"[8-9]{1}[0-9]{9}", val) and len(val) == 10:
        print('yes')
    else:
        print('no')

#Example5
#a blackslash is used to define special characters in regx

rr = re.match('\\\\', '\\author')
print(rr.group())

#unicode language
        
if re.match(u'ياسمين', u'ياسمين', re.UNICODE):
    print('match!')
else:
    print('not a match!')

#Search
#check for a match anywhere on the string
result = re.search(r'AV', 'AV Analytics vidhaya AV')
print(result)
print(result.group(0))

#/= any char but \n
red = re.search(r'..g', 'piiig')
print(red)
print(red.group(0))

#d = digit char, \w = word char
res = re.search(r'\d\d\d', 'p123')
print(res.group(0))
res = re.search(r'\w\w\w', '@!abd')
print(res.group(0))

#i+ = one or more i's, as many as possible
result  = re.search(r'pi+', 'piiiiiiiif')
if result:
    print(result.group())

#\s* = zero or more whitespace chars, ##here look for 3 digits, possibly separted y whitespace
result = re.search(r'\d\s*\d\s*\d', 'xx1 2    3xx')
print(result.group())

result = re.search(r'\d\s*\d\s*\d', 'xx12    3xx')
print(result.group())

result = re.search(r'\d\s*\d\s*\d', 'xx123xx')
print(result.group())

#^ = matches the start of string
result = re.search(r'b\w+', 'fooobar')
print(result.group())

#using pattern r'\w+@\w+'
str = 'purple alice=b@google.com monkey'
match = re.search(r'\w+@w+', str)
if match:
    print(match.group())

match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
    print(match.group())
