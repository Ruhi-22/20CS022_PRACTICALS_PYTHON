# PRACTICAL 2 -Study and Learn List, Tuple, Set and Dictionary
# By - RUHI KANSAGARA
# ID - 20CS022

# Dictionary
# 1.Write a Python script to check whether a given key already exists in a dictionary.
dict = {1:2,2:4,3:6,4:8,5:10}
key = 3
if key in dict:
    print(key,"is present")
else:
    print(key,"is not present")

# 2. Write a Python script to merge two Python dictionaries.
days_1 = {'Monday':1,'Tuesday':2,'Wednesday':3}
days_2 = {'Thursday':4,'Friday':5,'Saturday':6,'Sunday':7}
days_1.update(days_2)
print(days_1)

# 3.Write a Python program to sum all the items in a dictionary.
def returnSum(myDict):
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)

    return final

dict_num = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict_num))

# 4.Write a Python script to add a key to a dictionary.
dict1 = {1:10,2:20}
dict2 = {3:30}
dict1.update(dict2)
print(dict1)

# 5.Write a Python script to concatenate following dictionaries to create a new one.
#
# Sample Dictionary :
#
# dic1={1:10, 2:20}
#
# dic2={3:30, 4:40}
#
# dic3={5:50,6:60}
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic2.update(dic3)
dic1.update(dic2)
print(dic1)
