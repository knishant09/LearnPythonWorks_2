import os

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = set(("apple", "banana", "cherry"))

print(thisset)
thisset.add("test")

print(thisset)
print(len(thisset))

list_a = [1, 2, 3]
list_b = ['a', 'b', 'c', 'd', 'e']

zip_list = zip(list_a, list_b)

print(zip_list)

test2 = list(zip(list_a, list_b))

print(test2)
