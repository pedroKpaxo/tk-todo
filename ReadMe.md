# ToDo App

The ToDo App is a simple yet robust task management application built using Python's Tkinter for the graphical user interface (GUI) and SQLAlchemy for database management. This project adheres to the Model-View-Controller (MVC) design pattern, ensuring a clean separation of concerns, making the codebase modular, maintainable, and easy to extend.

# Features
- Add Tasks: Create new tasks with a title.
- View Tasks: Display tasks in a table format with columns for ID, Task, and Date Added.
- Delete Tasks: Remove tasks from the list.
- Responsive GUI: The interface adjusts to different window sizes, with input fields and tables expanding as needed.

# Project structure
```bash
todo_app/
│
├── abstract_controller.py    # Interface definition for the controller
├── controllers.py            # Implementation of the controller
├── main.py                   # Entry point of the application
├── models.py                 # Database models and setup
└── views.py                  # Tkinter-based GUI (View)
```

# Installation
clone the repository using git:

```bash
git clone https://github.com/yourusername/todo_app.git
cd todo_app
```
You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

and run the application using the following command:

```bash
python main.py
```

# Code Overview

## Models (models.py)
The Task model represents a task with the following attributes:

id: Primary key, auto-incremented.
task: The name of the task.
date: The timestamp when the task was added.

## Controller Interface (abstract_controller.py)
The ToDoControllerInterface defines the contract that any controller implementation must follow, including methods for adding, retrieving, and deleting tasks.

## View (views.py)
The ToDoView class is responsible for the GUI. It uses Tkinter's Treeview widget to display tasks and Entry widgets for user input. The layout is managed using the grid geometry manager, ensuring the interface is responsive and elements expand as needed.

## Main (main.py)
The main.py file is the entry point of the application. It initializes the controller and view, and starts the Tkinter main loop.

## Future Enhancements
- Task Editing: Add functionality to edit existing tasks.
- Task Filtering: Implement filtering options to display tasks based on specific criteria (e.g., date, keywords).
- Task Completion: Add a feature to mark tasks as completed.

# Building a Standalone Executable
You can create a standalone executable for the ToDo App using PyInstaller. First, install PyInstaller using pip:

```bash
pip install pyinstaller
```

Then, run the following command to create the executable:

```bash
make build
```