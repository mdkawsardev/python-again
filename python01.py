line = "hey! I'm md kawsar, I'm a full-stack web developer"
line.replace("kawsar", "imran")
print(line)
print(line.endswith("per"))
print(line.startswith("Hey"))
print(line.find("m")) # returns index number of the string
print(line.count("m")) # returns number of usage
print(line.upper())
print(line.lower())
print(line.capitalize())
print(line.title())
myList = ["Apple", "Banana", True, "Orange", 8, 9.0, "Cherry"]
myList[0] = "Coconute"
myList.append("Animal")
myList.reverse()
myList.pop(1) # removes by index number
myList.remove("Banana") # removes by items name
print(myList)
line2 = "hey! I'm md kawsar, I'm a full-stack web developer"
line3 = line2.split()
for i in line3:
    print(i)