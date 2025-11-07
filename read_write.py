with open("write_file.txt") as f:
    content = f.read()

with open("read_file.txt", "w") as f:
    f.write(content)