import sys

def fetch_numbers(x, y, z):

    print x, y, z
    if int(x) == int(y) == int(z):
        sum = ((int(x) * 3) * 3)
        print sum
    else:
        sum1 = int(x) + int(y) + int(z)
        print sum1


fetch_numbers(sys.argv[1], sys.argv[2], sys.argv[3])






