#A Set in Python programming is an unordered collection data type that is iterable, mutable and has no duplicate elements.
#The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set.

a = {1, 2, 3, 4, 5, 5}
len(a)
a.add(10)
a.update([12, 23, 89]) #add multiple values
a.remove(12)
a.pop() #remove the first value

name = {'max', 'dkdk', 'ldkd'}
name.clear()
name

name = set(('max', 'dkdk', 'ldkd')) # convert tuples set

name = set(['max', 'dkdk', 'ldkd']) # convert lists to set

b = {1, 2, 3, 4, 5}

a | b # union set (a or b)
a.union(b)

a & b #it returns the similar value in a and b
a - b #it return the element whose in a and not in b

a.difference(b) #whats on a and not in b
a.symmetric_difference(b)