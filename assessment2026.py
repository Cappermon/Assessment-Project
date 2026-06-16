import json
#Imports the json library
# load saved to-do lists from the library
try:
    file = open("todo.txt", "r") #Opens file in read mode
    lists = json.load(file) #Converts json data into a dictionary
    file.close() #closes the file
except:
    lists = {} #creates an empty dictionary if file doesnt exist
#Main program loop
while True:
    #displays main menu being the list options
    print("\nTO DO LIST")
    print("1. Create list")
    print("2. Delete list")
    print("3. View lists")
    print("4. Open list")
    print("5. Exit")

    choice = input("Choose: ")
#creates new list
    if choice == "1":
        name = input("List name: ")
        lists[name] = []
#Delete an existing list
    elif choice == "2":
        print(lists)
        name = input("Delete which list: ")
        if name in lists:
            del lists[name]
#Display all list names
    elif choice == "3":
        for l in lists:
            print(l)
#Open a selected list
    elif choice == "4":
        name = input("Enter list name: ")
        if name in lists:
#List management menu
            while True:
                print("\n", name)
                print("1. Add item")
                print("2. Remove item")
                print("3. Mark complete")
                print("4. View items")
                print("5. Back")

                sub = input("Choose: ")
#Add a task to the list
                if sub == "1":
                    task = input("Enter task: ")
                    lists[name].append([task, False])
#Remove a task from the list
                elif sub == "2":
                    for i in range(len(lists[name])):
                        print(i+1, lists[name][i])
                    num = int(input("Item number: ")) - 1
                    if num >= 0 and num < len(lists[name]):
                        lists[name].pop(num)
#Mark a task as completed
                elif sub == "3":
                    for i in range(len(lists[name])):
                        print(i+1, lists[name][i])
                    num = int(input("Item number: ")) - 1
                    if num >= 0 and num < len(lists[name]):
                        lists[name][num][1] = True
#View all items in the list and their status
                elif sub == "4":
                    for item in lists[name]:
                        if item[1] == True:
                            print("[✓]", item[0])
                        else:
                            print("[ ]", item[0])
#Return to main menu
                elif sub == "5":
                    break
#Exit the Program
    elif choice == "5":
        break

    # Save every loop
    file = open("todo.txt", "w")
    json.dump(lists, file)
    file.close()