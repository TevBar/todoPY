Todo List Application
This is a command-line Todo List Application implemented in Python. The app allows users to manage multiple lists and tasks within each list. It saves data locally to retain progress between sessions.

Features
Create Lists: Add new todo lists.
Add Tasks: Add tasks to any selected list.
Mark Task Completion: Mark tasks as complete or incomplete.
Clear Completed Tasks: Remove all completed tasks from a selected list.
Delete Lists: Delete any selected list and its tasks.
Local Storage: Saves your lists and tasks to JSON files for persistence.
Requirements
Python 3.x
JSON (Python Standard Library)
Compatible with Windows, macOS, and Linux operating systems.
Setup and Usage
Clone or Download the Repository:

bash
Copy code
git clone https://github.com/your-username/todo-list-app.git
cd todo-list-app
Run the Application: To start the application, open a terminal in the project directory and run:

bash
Copy code
python todo_app.py
Using the Application:

The application displays your existing lists and allows you to add, select, or delete lists and tasks.
After selecting a list, you can:
Add new tasks
Toggle task completion
Clear completed tasks
All changes are saved automatically to the lists.json and selected_list_id.json files.
Available Commands
After launching the app, you’ll see the following options:

1. Add a new list: Creates a new list.
2. Add a task to the selected list: Adds a task to the currently selected list.
3. Toggle a task’s completion: Marks a task as complete or incomplete.
4. Select a list: Sets a specific list as active, allowing you to add and manage tasks within it.
5. Delete the selected list: Removes the current list and its associated tasks.
6. Clear completed tasks from the selected list: Deletes all completed tasks in the active list.
7. Quit: Exits the application and saves data.
Data Storage
The application uses two JSON files for storing data:

lists.json: Stores all lists and tasks.
selected_list_id.json: Stores the ID of the currently selected list.
Error Handling
Each operation in the menu is wrapped in a try-except block to manage errors gracefully. If an error occurs, an error message will be printed without interrupting the app.
Thank You
Thank you for using this Todo List Application! If you have any feedback or encounter issues, feel free to reach out.

