import sys



x, y = 10, 20
print(x, y)
x, y = y, x
print(x, y)

a ="GeeksForGeeks"
print("Reverse is", a[:-1])
print("Reverse is", a[::-1])

a = ["Geeks", "For", "Geeks"]
print(" ".join(a))

n = 10
result = 1 < n < 20
print(result)
result = 1 > n <= 9
print(result)

import os
import socket

print(os)
print(socket)


class MyName:
    Geeks, For, Geeks = range(3)

print(MyName.Geeks)
print(MyName.For)
print(MyName.Geeks)




