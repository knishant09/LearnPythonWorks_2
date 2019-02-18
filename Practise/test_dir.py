import os



class Hello:

    def __dir__(self):
        return [1,2,3]

t =  Hello()

print(dir(Hello(t)))

number = [1, 2, 3]
print(dir(number))

print('\nReturn Value from empty dir()')
print(dir())


class Person:
    def __dir__(self):
        return ['age', 'name', 'salary']


teacher = Person()
print(dir(teacher))