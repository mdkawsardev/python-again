a = 23
b = 50
c = 44

print((a + b + c)/3) # Average number of these 3 numbers

def greet():
    return("Good morning")
print(greet())

# factorial of input number
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)
n = int(input("Enter a number: "))
print(factorial(n))