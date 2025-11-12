with open("write_file.txt") as f:
    content = f.read()

with open("read_file.txt", "w") as f:
    f.write(content)


with open("message.txt") as f:
    print(f.read())
txt = "I wanna say something"
with open("message.txt", "w") as w:
    w.write(txt) # Remember one thing, when you write something to the file, previous texts will be overwritten by new texts