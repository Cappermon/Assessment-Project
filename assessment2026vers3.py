import tkinter as tk
from tkinter import simpledialog, messagebox
import json

# Load data
try:
    with open("todo.txt", "r") as file:
        lists = json.load(file)
except:
    lists = {}

current_list = None

# Save data
def save_data():
    with open("todo.txt", "w") as file:
        json.dump(lists, file)

# Refresh list names
def update_lists():
    listbox_lists.delete(0, tk.END)
    for name in lists:
        listbox_lists.insert(tk.END, name)

# Refresh tasks
def update_tasks():
    listbox_tasks.delete(0, tk.END)

    if current_list:
        for task, complete in lists[current_list]:
            if complete:
                listbox_tasks.insert(tk.END, f"✓ {task}")
            else:
                listbox_tasks.insert(tk.END, f"☐ {task}")

# Create list
def create_list():
    name = simpledialog.askstring("New List", "List name:")

    # Check if user cancelled or left it blank
    if not name or name.strip() == "":
        messagebox.showerror("Error", "Please enter a list name.")
        return

    # Check for duplicate list names
    if name in lists:
        messagebox.showerror("Error", "A list with that name already exists.")
        return

    lists[name] = []
    save_data()
    update_lists()

# Delete list
def delete_list():
    selection = listbox_lists.curselection()

    if selection:
        name = listbox_lists.get(selection[0])
        del lists[name]
        save_data()
        update_lists()
        listbox_tasks.delete(0, tk.END)

# Open list
def open_list():
    global current_list

    selection = listbox_lists.curselection()

    if selection:
        current_list = listbox_lists.get(selection[0])
        update_tasks()

# Add task
def add_task():
    if not current_list:
        messagebox.showerror("Error", "Open a list first")
        return

    task = simpledialog.askstring("Add Task", "Task name:")

    # Check for blank task names
    if not task or task.strip() == "":
        messagebox.showerror("Error", "Please enter a task name.")
        return

    lists[current_list].append([task, False])
    save_data()
    update_tasks()

# Remove task
def remove_task():
    if not current_list:
        return

    selection = listbox_tasks.curselection()

    if selection:
        lists[current_list].pop(selection[0])
        save_data()
        update_tasks()

# Mark complete
def complete_task():
    if not current_list:
        return

    selection = listbox_tasks.curselection()

    if selection:
        index = selection[0]
        lists[current_list][index][1] = True
        save_data()
        update_tasks()

# Window
root = tk.Tk()
root.title("To Do List")
root.geometry("900x600")
root.configure(bg="#1E293B")

# Title
title = tk.Label(
    root,
    text="📋 To Do List Manager",
    font=("Arial", 24, "bold"),
    bg="#1E293B",
    fg="white"
)
title.pack(fill="x", pady=10)

# Main container
main_frame = tk.Frame(root, bg="#1E293B")
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Left Panel - Lists
frame_left = tk.Frame(
    main_frame,
    bg="#334E68",
    bd=3,
    relief="ridge"
)
frame_left.pack(side=tk.LEFT, fill="both", expand=True, padx=10)

tk.Label(
    frame_left,
    text="Lists",
    font=("Arial", 18, "bold"),
    bg="#334E68",
    fg="white"
).pack(pady=10)

listbox_lists = tk.Listbox(
    frame_left,
    width=25,
    height=15,
    bg="#F8FAFC",
    fg="black",
    font=("Arial", 15)
)
listbox_lists.pack(fill="both", expand=True, padx=10, pady=10)

tk.Button(
    frame_left,
    text="Create List",
    bg="#334E68",
    fg="black",
    font=("Arial", 12, "bold"),
    command=create_list
).pack(fill="x", padx=10, pady=5)

tk.Button(
    frame_left,
    text="Delete List",
    bg="#334E68",
    fg="black",
    font=("Arial", 12, "bold"),
    command=delete_list
).pack(fill="x", padx=10, pady=5)

tk.Button(
    frame_left,
    text="Open List",
    bg="#334E68",
    fg="black",
    font=("Arial", 12, "bold"),
    command=open_list
).pack(fill="x", padx=10, pady=5)

# Right Panel - Tasks
frame_right = tk.Frame(
    main_frame,
    bg="#334E68",
    bd=3,
    relief="ridge"
)
frame_right.pack(side=tk.RIGHT, fill="both", expand=True, padx=10)

tk.Label(
    frame_right,
    text="Tasks",
    font=("Arial", 18, "bold"),
    bg="#334E68",
    fg="white"
).pack(pady=10)

listbox_tasks = tk.Listbox(
    frame_right,
    width=40,
    height=15,
    bg="#F8FAFC",
    fg="black",
    font=("Arial", 15)
)
listbox_tasks.pack(fill="both", expand=True, padx=10, pady=10)

tk.Button(
    frame_right,
    text="Add Task",
    bg="#334E68",
    fg="black",
    font=("Arial", 12, "bold"),
    command=add_task
).pack(fill="x", padx=10, pady=5)

tk.Button(
    frame_right,
    text="Remove Task",
    bg="#334E68",
    fg="black",
    font=("Arial", 12, "bold"),
    command=remove_task
).pack(fill="x", padx=10, pady=5)

tk.Button(
    frame_right,
    text="Mark Complete",
    bg="#334E68",
    fg="black",
    font=("Arial", 12, "bold"),
    command=complete_task
).pack(fill="x", padx=10, pady=5)

# Status bar
status = tk.Label(
    root,
    text="Ready",
    bg="#0F172A",
    fg="white"
)
status.pack(side="bottom", fill="x")

update_lists()
root.mainloop()