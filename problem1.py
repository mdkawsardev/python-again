n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1))

for i in range(1, 11):
    print(f"{n} X {11 - i} = {n*(11 -i)}")
