import os
from array import *

class Array_test():

    def __init__(self):
        pass

    def array_file1(self):
        T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]

        print(T[0])

        print(T[1][2])

        T.insert(2, [0,4,3,5])

        for r in T:
            for c in r:
                print(c, end = " ")
            print()

        Months = set(["Jan", "Feb", "Mar"])
        Months.add("Apr")
        print(Months)
        Months.discard("Feb")
        print(Months)
        Month1 = set(["Dec", "Nov", "Jan"])
        Allmonths =  Months|Month1
        print(Allmonths)
        All_m = Month1 - Months
        print(All_m)
        

obj= Array_test()

obj.array_file1()





