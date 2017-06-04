#Import module
from collections import Counter

print('Counter() Method')
#Counter with Numbers
l = [1,1,12,3,213,12,32,2,4,5,6,3,2,1]
print(Counter(l))

#Counter with string
s = "Vo Hoang Gia Bao"
print(Counter(s))

#Counter with word
senten = "How many times does each word show up in this sentence word times each each word"
senten_split = senten.split()
print(Counter(senten_split))

#Method of Counter
c = Counter(senten_split)
print(c.most_common(3))

#Common patterns method
'''
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts
'''