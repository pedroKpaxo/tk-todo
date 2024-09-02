import tkinter as tk
from tkinter import ttk
from abstract_controller import ToDoControllerInterface

import ctypes
import os
import platform


class ToDoView(tk.Tk):
    def __init__(self, controller: ToDoControllerInterface):
        super().__init__()
        self.controller = controller

        self.title("ToDo App")
        self.geometry("500x400")
        icon = tk.PhotoImage(file="icon.png")
        self.iconphoto(True, icon)

        # Configure grid layout for more control over widget positioning
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.check_platform()
        self.create_widgets()
        # Load existing tasks
        self.load_tasks()

    def check_platform(self):
        system_platform = platform.system()

        if system_platform == "Windows":
            # Set the icon using .ico file
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("ToDo App")
            icon_path = os.path.join(os.path.dirname(__file__), 'icon.png')
            icon = tk.PhotoImage(file=icon_path)
            self.iconphoto(False, icon)

        elif system_platform == "Linux" or system_platform == "Darwin":
            # Set the icon using .png file
            icon_path = os.path.join(os.path.dirname(__file__), 'icon.png')
            icon = tk.PhotoImage(file=icon_path)
            self.iconphoto(False, icon)

    def create_widgets(self):

        # Task input
        self.task_label = tk.Label(self, text="Task")
        self.task_label.grid(row=0, column=0, padx=5, sticky="w")

        self.task_entry = tk.Entry(self)
        self.task_entry.grid(row=1, column=0, padx=5, sticky="nsew")

        # Add Task button
        self.add_task_button = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=2, column=0, padx=5, sticky="ew")

        # Treeview for tasks
        self.tasks_tree = ttk.Treeview(self, columns=("ID", "Task", "Date"), show="headings")
        self.tasks_tree.heading("ID", text="ID")
        self.tasks_tree.heading("Task", text="Task")
        self.tasks_tree.heading("Date", text="Date Added")

        # Set column widths
        self.tasks_tree.column("ID", width=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tasks_tree.column("Task", width=200, stretch=tk.YES)
        self.tasks_tree.column("Date", width=200, stretch=tk.YES)

        self.tasks_tree.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

        # Delete Task button
        self.delete_task_button = tk.Button(self, text="Delete Task", command=self.delete_task)
        self.delete_task_button.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.controller.add_task(task)
            self.task_entry.delete(0, tk.END)
            self.load_tasks()

    def delete_task(self):
        selected_item = self.tasks_tree.selection()
        if selected_item:
            task_id = self.tasks_tree.item(selected_item)["values"][0]
            self.controller.delete_task(task_id)
            self.load_tasks()

    def load_tasks(self):
        # Clear the treeview
        for item in self.tasks_tree.get_children():
            self.tasks_tree.delete(item)

        # Insert tasks into the treeview
        tasks = self.controller.get_tasks()
        for task in tasks:
            self.tasks_tree.insert("", tk.END, values=(task.id, task.task, task.date))
