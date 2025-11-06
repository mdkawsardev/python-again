for i in range(10):
    if(i == 4):
        break # Exits the loop right now
    print(i)
print("")
for i in range(10):
    if(i == 4):
        continue # Skips the iteration
    print(i)
for i in range(10):
    pass # I will work here next

# Multiplication of user input from 1 to 10
user = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{user} X {i} = {user * i}")

# Same operation with while loop
k = 1
while(k < 11):
    print(f"{user} X {k} = {user * k}")
    k +=1

l = ["kawsar", "imran", "sumon", "jahid", "imo", "kamrul"]
for name in l:
    if(name.startswith("k")): # checks the items which starts with k
        print(f"Hello {name}")