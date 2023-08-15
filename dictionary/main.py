#dictionaries are mutable data structures that allow you to store key-value pairs.
#Dictionary can be created using the dict() constructor or curly braces' {}'. Once you have created a dictionary, you can add, remove, or update elements using the methods dict. update(), dict. pop(), and dict

d = {'name' : 'yasmine', 'year' : 2023}
d['name']

d['surname'] = 'yasumin' #adding
d.pop('username') #deleting
d.clear() #clear
del d