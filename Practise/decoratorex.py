import os


def toppings(func):
    def inner(*args):
        print(*args)
        print("adding extra toppings")
        func(*args)

    return inner

class Pizza():

    def __init__(self, **kwargs):
        print(kwargs)
        self.psize = kwargs.get('psize')
        self.ptype = kwargs.get('ptype')
        self.porder = kwargs.get('porder')

        print(self.psize)

    def toppings1(func):
        def inner(*args):
            print(*args)
            print("adding extra toppings")
            func(*args)

        return inner




    @toppings
    def prepare_pizza(self):
        print("Preparing")

    @toppings1
    def order_pizza(self):
        print("Testing order pizza")
        print(self)






obj = Pizza(psize="medium", ptype="veg", porder="online")

obj.prepare_pizza()
obj.order_pizza()

