a = 23
b = 50
c = 44

print((a + b + c)/3) # Average number of these 3 numbers

def greet():
    return("Good morning")
print(greet())
'''
factorial(0) = 1
factorial(1) = 1x1 = 1
factorial(2) = 2x1 = 2
factorial(3) = 3x2x1 = 6
factorial(4) = 4x3x2x1 = 24
factorial(5) = 5x4x3x2x1 = 120
'''
d = '''
the 
apple
choice
'''
# factorial of input number
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)
n = int(input("Enter a number: "))
print(factorial(n))
