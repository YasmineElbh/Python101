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