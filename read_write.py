# open("file_name", "r,w,a")
with open("write_file.txt") as f: # when a file is open for reading then open("file_name") second parameter by default r
    content = f.read()

with open("read_file.txt", "w") as f: # when a file is open for writing then open("file_name", "w") second parameter is w
    f.write(content)


with open("message.txt") as f:
    print(f.read())
txt = "I wanna say something"
with open("message.txt", "w") as w:
    w.write(txt) # Remember one thing, when you write something to the file, previous texts will be overwritten by new texts