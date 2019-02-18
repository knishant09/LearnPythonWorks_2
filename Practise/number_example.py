import os


a = "131"

b = reversed(a)

print(b)

if list(a) == list(b):
    print("Palindrome")
else:
    print("Not a palindrome")

num = input("Enter any number: ")
print(type(num))
rev_num = reversed(num)
# check if the string is equal to its reverse
if list(num) == list(rev_num):
             print("Palindrome number")
else:
             print("Not Palindrome number")

def fun(n):
   """Recursive function to
   print Fibonacci sequence"""
   if n <= 1:
       return n
   else:
       return(fun(n-1) + fun(n-2))

# receive input from the user
terms = int(input("How many terms U want Fibonacci ?: "))

if terms <= 0:
   print("Plese enter only positive integer")
else:
   print("Fibonacci Series:")
   for i in range(terms):
       print(fun(i))

for g in range (6,0,-1):
    print(g * ' ' + (6-g) * '*')



def pypart(n):
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")

        # ending line after each row
        print("\r")


# Driver Code
n = 5
pypart(n)