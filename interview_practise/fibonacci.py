import os


def fib(n):
    if (n <=1):
        return n
    else:
        return(fib(n-1) + fib(n-2))

n = int(input("enter the number:"))

print(n)

for i in range(n):
    print(fib(i))

