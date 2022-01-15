# PRACTICAL 2 -Study and Learn List, Tuple, Set and Dictionary
# By - RUHI KANSAGARA
# ID - 20CS022

# Sets
# 1.Write a Python program to add member(s) in a set and clear a set
from typing import Set

languages = {'C','C++','HTML','Java'}
languages.add('Python')
print(languages)
languages.clear()
print(languages)

# 2.Write a Python program to remove an item from a set if it is present in the set.
Numbers = {10,20,30,40,50}
Numbers.remove(30)
print(Numbers)

# 3.Write a Python program to create an intersection, Union, difference of sets.
A = {1,2,3,4,5}
B = {1,6,2,7,3}
numbers = A.union(B)
print(numbers)
intersection_num = A.intersection(B)
print(intersection_num)
print(A.difference(B))

# 4.Write a Python program to find maximum and the minimum value in a set.
Set_num = {75,100,45,89,110}
print(max(Set_num))
print(min(Set_num))

# 5.
# E) Write a Python program to find the most common elements and their counts from list, tuple, dictionary
print('LIST')
words=['yellow', 'green', 'blue', 'yellow','yellow','green']
print('list:',words)
from collections import Counter
c = Counter(words)
c.most_common(1)
print ('the most common element from the list :',c.most_common(1))

print('TUPLE')
words=('apple', 'grapes', 'cherry', 'grapes','cherry','orange')
print('tuple:',words)
from collections import Counter
c = Counter(words)
c.most_common(1)
print ('the most common element from the tuple :',c.most_common(1))

print('DICTIONARY')
word={'school':1, 'home':2, 'hospital':3,'school':4}
from collections import Counter
c = Counter(word)
c.most_common(1)
print ('the most common element from the dict :',c.most_common(1))