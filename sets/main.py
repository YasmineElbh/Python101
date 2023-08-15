

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