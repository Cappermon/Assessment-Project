import tkinter as tk
from tkinter import simpledialog, messagebox
import json

# Load data
try:
    with open("todo.txt", "r") as file:
        lists = json.load(file)
except:
    lists = {}
