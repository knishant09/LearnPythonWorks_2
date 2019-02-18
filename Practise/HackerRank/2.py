import sys


def weired_notweired(num):
    print(num)

    if num % 2 != 0:
        print("Number is odd:{}".format(num))
        print("Weird")
    elif num % 2 == 0 and 2 <= num <= 5:
        print("Not Weird")
    elif num % 2 == 0 and 6 <= num <= 20:
        print("Weird")
    elif num % 2 == 0 and num > 20:
        print("Not Weird")



num = int(input("enter the number between 1 and 100:"))

if 1 <= num <= 100:
    weired_notweired(num)

else:
    print("Range is between 1 and 100")