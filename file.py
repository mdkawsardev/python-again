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