import json
import os
from datetime import datetime

# Simulated "localStorage" keys for Python
LOCAL_STORAGE_LIST_KEY = 'task_lists.json'
LOCAL_STORAGE_SELECTED_LIST_ID_KEY = 'selected_list_id.json'

# Load lists and selected list ID from a JSON file
def load_data():
    try:
        if os.path.exists(LOCAL_STORAGE_LIST_KEY):
            with open(LOCAL_STORAGE_LIST_KEY, 'r') as file:
                lists = json.load(file)
        else:
            lists = []
        
        if os.path.exists(LOCAL_STORAGE_SELECTED_LIST_ID_KEY):
            with open(LOCAL_STORAGE_SELECTED_LIST_ID_KEY, 'r') as file:
                selected_list_id = json.load(file)
        else:
            selected_list_id = None
        
        return lists, selected_list_id
    except Exception as e:
        print(f"Error loading data: {e}")
        return [], None

# Save lists and selected list ID to a JSON file
def save_data(lists, selected_list_id):
    try:
        with open(LOCAL_STORAGE_LIST_KEY, 'w') as file:
            json.dump(lists, file)
        
        with open(LOCAL_STORAGE_SELECTED_LIST_ID_KEY, 'w') as file:
            json.dump(selected_list_id, file)
    except Exception as e:
        print(f"Error saving data: {e}")

# Create a new list
def create_list(name):
    return {"id": str(datetime.now().timestamp()), "name": name, "tasks": []}

# Create a new task
def create_task(name):
    return {"id": str(datetime.now().timestamp()), "name": name, "complete": False}

# Render lists and tasks
def render(lists, selected_list_id):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Todo Lists:\n")
    for list_item in lists:
        prefix = "[Selected]" if list_item['id'] == selected_list_id else ""
        print(f"{list_item['name']} {prefix}")

    selected_list = next((lst for lst in lists if lst['id'] == selected_list_id), None)
    if selected_list:
        print(f"\nTasks in '{selected_list['name']}':")
        for task in selected_list['tasks']:
            status = "Done" if task['complete'] else "Not Done"
            print(f"{task['name']} - {status}")
    else:
        print("\nNo list selected.")

# Main program loop
def main():
    lists, selected_list_id = load_data()

    while True:
        render(lists, selected_list_id)
        
        print("\nOptions:")
        print("1: Add List")
        print("2: Add Task to Selected List")
        print("3: Toggle Task Completion")
        print("4: Select List")
        print("5: Delete Selected List")
        print("6: Clear Completed Tasks")
        print("7: Quit")
        
        choice = input("Choose an option: ")
        
        try:
            if choice == "1":
                list_name = input("Enter list name: ")
                if list_name:
                    lists.append(create_list(list_name))
                    save_data(lists, selected_list_id)
            elif choice == "2":
                if selected_list_id:
                    task_name = input("Enter task name: ")
                    if task_name:
                        selected_list = next((lst for lst in lists if lst['id'] == selected_list_id), None)
                        if selected_list:
                            selected_list['tasks'].append(create_task(task_name))
                            save_data(lists, selected_list_id)
                else:
                    print("Select a list first.")
            elif choice == "3":
                if selected_list_id:
                    task_name = input("Enter task name to toggle: ")
                    selected_list = next((lst for lst in lists if lst['id'] == selected_list_id), None)
                    task = next((task for task in selected_list['tasks'] if task['name'] == task_name), None)
                    if task:
                        task['complete'] = not task['complete']
                        save_data(lists, selected_list_id)
                    else:
                        print("Task not found.")
            elif choice == "4":
                list_name = input("Enter list name to select: ")
                selected_list = next((lst for lst in lists if lst['name'] == list_name), None)
                if selected_list:
                    selected_list_id = selected_list['id']
                    save_data(lists, selected_list_id)
                else:
                    print("List not found.")
            elif choice == "5":
                lists = [lst for lst in lists if lst['id'] != selected_list_id]
                selected_list_id = None
                save_data(lists, selected_list_id)
            elif choice == "6":
                selected_list = next((lst for lst in lists if lst['id'] == selected_list_id), None)
                if selected_list:
                    selected_list['tasks'] = [task for task in selected_list['tasks'] if not task['complete']]
                    save_data(lists, selected_list_id)
            elif choice == "7":
                print("Thank you for using the Todo App.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
