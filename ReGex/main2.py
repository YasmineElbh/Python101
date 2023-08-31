import re

#allow upperCase
pattern = re.compile("^[A-Z]+$")
print(pattern.search('Hello World'))
print(pattern.search('hello world'))
print(pattern.match('helloworld'))

#3 lowerCase
#3-5 digits
#one symbol
#up to two uppercase characte(optional)
pattern = re.compile("^[a-z]{3}[0-9]{3,5}[^a-zA-Z0-9]{1}[A-Z]{0,2}$")
print(pattern.search('Hello257#6'))
print(pattern.search('lll44511.k'))
print(pattern.match('hel123456#JJ'))

