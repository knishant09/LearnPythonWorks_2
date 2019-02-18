import os


def thousand(n):
    return (((abs(1000-n)) <= 100) or (abs(2000 -n) <= 100))





print(thousand(1000))
print(thousand(900))
print(thousand(800))
print(thousand(2200))