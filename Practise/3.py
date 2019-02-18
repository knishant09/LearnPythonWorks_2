import os,sys, math

pi = 3.145

def area(radius):
    print str(radius)

    A = str(pi * radius ** 2)
    return A


if __name__ == "__main__":
    radius = float(raw_input("enter the radius of a circle"))
    A = area(radius)
    print "Area of a circle is: %s" %A