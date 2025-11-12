from random import choice
def myfunc(x):
    return x*x
print(myfunc(5))

# This is same as above function. Lambda is a short way to write in a sinlge line of code
func = lambda x: x*x # lambda a an anonymous function
print(func(5))

l = ["kawsar", "imran", "emon", "asif"]

print(choice(l))