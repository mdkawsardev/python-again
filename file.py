# Reading a file
file = open("text.txt", "r")
read = file.read()
print(read)
file.close()

# Writing a file
description = "Hello sir, You have been hired to our company"
f = open("message.txt", "w")
f.write(description)
f.close()

# Reading files using with statement, and no need to close files
with open("message.txt", "r") as op:
    print(op.read())

open_file = open("multiline.txt", "r")
read_file = open_file.readlines() # This reads line by line and returns a list
print(type(read_file)) # This type is a list
for i in read_file:
    print(i, end="")

# read_file = open_file.readline() # This reads just a single line
# print(read_file)

# It will append line for 10 times
x = 0
while x < 10:
    open_for_append_line = open("message.txt", "a") # a means => append the lines end of the previous line of the file
    open_for_append_line.write(description)
    open_for_append_line.close()
    x += 1