# PRACTICAL 2 -Study and Learn List, Tuple, Set and Dictionary
# By - RUHI KANSAGARA
# ID - 20CS022

# Tuple
# 1.Write a Python program to create a tuple with different data types.
tuple1 = ('Python',24,16.03,True)
print(tuple1)

# 2.Write a Python program to create a tuple with numbers and print one item.
Numbers = (10,20,30,40,50)
print(Numbers[0])

# 3.Write a Python program to add an item in a tuple.
Companies = ('Amazon','Oracle','TCS','Microsoft')
x = ('Infosys',)
Companies = Companies + x
print(Companies)

# 4.Write a Python program to convert a tuple to a string.
letters = ('P','y','t','h','o','n')
y = "".join(letters)
print(y)

# 5.Write a Python program to find the length of a tuple.
print(len(Companies))