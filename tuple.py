# marks = []
# for i in range(6):
#     while True:
#         try:
#             user = int(input(f"Enter your number: "))
#             i +=1
#             marks.append(user)
#             break
#         except ValueError:
#             print("Invalid input")
# marks.sort()
# print(marks)

result = {
    "kawsar": {
        "Bangla": 89,
        "English": 99,
        "Math": 87,
        "History": 76
    },
    "imran": {
        "Bangla": 65,
        "English": 45,
        "Math": 67,
        "History": 77
    },
    "sumon": {
        "Bangla": 88,
        "English": 65,
        "Math": 98,
        "History": 45
    },
    "jahid": {
        "Bangla": 47,
        "English": 54,
        "Math": 98,
        "History": 65
    },
    "mitul": {
        "Bangla": 94,
        "English": 90,
        "Math": 33,
        "History": 66
    }
}

# user = input("Enter your name: ")
# for name in result:
#     run = True
#     while run:
#         if user == name:
#             run = False
#             print(f"Hello {user} your marks bellow:")
#         for n in result[user]:
#             print(f"{n} = {result[user][n]}")

# while True:
#     user_input = input("Type your command: ")
#     if user_input.lower() == "get my record":
#         print("Fetching your record...")
#         break
#     else:
#         print("Unrecognized command. Try again.")

# for name in result:

d = {}
name = input("Enter your name: ")
lang = input("Enter your language: ")
d.update({name: lang})
name = input("Enter your name: ")
lang = input("Enter your language: ")
d.update({name: lang})
name = input("Enter your name: ")
lang = input("Enter your language: ")
d.update({name: lang})
name = input("Enter your name: ")
lang = input("Enter your language: ")
d.update({name: lang})
print(d)