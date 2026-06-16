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
    if name:
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

    if task:
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

        