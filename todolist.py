import json

# load data
try:
    file = open("todo.txt", "r")
    lists = json.load(file)
    file.close()
except:
    lists = {}

while True:
    print("\nTO DO LIST")
    print("1. Create list")
    print("2. Delete list")
    print("3. View lists")
    print("4. Open list")
    print("5. Exit")