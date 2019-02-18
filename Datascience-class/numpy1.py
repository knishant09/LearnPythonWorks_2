import numpy as  np
import time
import json, jsondiff
from jsondiff import diff


arr1 = [1,2, 3]
arr2 = [5, 6, 7]

ar = np.array([arr1, arr2])
print(ar)

print(type(ar))

now = time.time()

age = 40 * 86400

print(age)

print(now)

t = now - age
print(t)

j1 = {"name": "John", age: 31, "city": "New York"}
json_t = json.dumps(j1)

print(j1)
print(json_t)

j2 = {"name": "John1", age: 31, "city": "New York"}

json_t1 = json.dumps(j2)

print(j2)
print(json_t1)

dif = diff(json_t, json_t1)

print("*********")
print(dif)

if dif:
    print("Diff found")
else:
    print("Same")
