[x for x in range(1,10) if x%3]              #for-if one line    x%3 is true for x cannot divide 3
#Out: [1,2,4,5,7,8]

[x if x%3 else 100*x for x in range(1,10)]               # if-else-for in one line
#Out: [1,2,300,4,5,600,7,8,900]


L1 = set('aabcd') #L1 = set(['a','b','c','d'])
L2 = set('cb')
L2.issubset(L1) # True

# sort a list
a = range(1,7)
sorted(a)
a.sort()

# slicing
a = range(1,7) #[1,2,3,4,5,6]
a[0:6:1] #a[start:end:step] start,end are both indexes, end is not included
a[0:5] #[1,2,3,4,5] index 5 stands for 6, but 6 is not included
a[:-2:] #[1,2,3,4] index -2 stands for 5
a[::-1] #[6,5,4,3,2,1]

# split strings according to ' '
a = 'hello world'
b = a.split() #b = ['hello','world']

# join strings in a list
c = ' '.join(b) #c = 'helloworld'

# dictionary operations
d = {'a':1}
key = 'a'
d.get(key,'') # return d['a']
key = 'b'
d.get(key,'') # return ''

# special dictionary
s = 'apple'
d = collections.Counter(s)
