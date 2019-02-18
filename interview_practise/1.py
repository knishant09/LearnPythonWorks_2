import os



def decor(func):
    def wrap():
        print("$$$$$$$$$$$$$$$$$$$$$")
        func()
        print("$$$$$$$$$$$$$$$$$")

@decor
def sayhi():
    print("hi")


newfunc = decor(sayhi)

newfunc()


