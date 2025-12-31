# To-Do List Manager
import json
from datetime import datetime
import matplotlib.pyplot as plt


FILE_NAME = "tasks.json"
#Load tasks
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

#Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

#Add task 
def add_task(tasks):
    desc = input("Enter task description: ")
    due = input("Enter due date (YYYY-MM-DD) or leave empty: ")

    if due:
        try:
            datetime.strptime(due, "%Y-%m-%d")
        except ValueError:
            print("Invalid date! Task will be saved without due date.")
            due = ""

    task = {
        "description": desc,
        "due_date": due,
        "status": "Pending"
    }
    tasks.append(task)
    print("Task added successfully!")

#View tasks 
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nTask List")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['description']} | Due: {task['due_date']} | Status: {task['status']}")

#View pending tasks 
def view_pending(tasks):
    print("\nPending Tasks")
    for i, task in enumerate(tasks, start=1):
        if task["status"] == "Pending":
            print(f"{i}. {task['description']} | Due: {task['due_date']}")

#View completed tasks
def view_completed(tasks):
    print("\nCompleted Tasks")
    for i, task in enumerate(tasks, start=1):
        if task["status"] == "Completed":
            print(f"{i}. {task['description']}")

#View tasks
def view_due_soon(tasks):
    print("\nTasks Due Soon (Next 7 days)")
    today = datetime.now()
    for i, task in enumerate(tasks, start=1):
        if task["due_date"]:
            try:
                due_date = datetime.strptime(task["due_date"], "%Y-%m-%d")
                if 0 <= (due_date - today).days <= 7:
                    print(f"{i}. {task['description']} | Due: {task['due_date']}")
            except ValueError:
                continue 

#Complete task 
def complete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark completed: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["status"] = "Completed"
            print("Task marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

#Edit task 
def edit_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to edit: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["description"] = input("Enter new description: ")
            due = input("Enter new due date (YYYY-MM-DD) or leave empty: ")
            if due:
                try:
                    datetime.strptime(due, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date! Due date will be cleared.")
                    due = ""
            tasks[num]["due_date"] = due
            print("Task updated!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

#Delete task 
def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            tasks.pop(num)
            print("Task deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Graphical summary 
def show_graph(tasks):
    completed = sum(1 for task in tasks if task["status"] == "Completed")
    pending = sum(1 for task in tasks if task["status"] == "Pending")
    
    plt.bar(["Completed", "Pending"], [completed, pending], color=["green", "red"])
    plt.title("Task Status Summary")
    plt.ylabel("Number of Tasks")
    plt.show()

#Main menu 
def menu():
    tasks = load_tasks()
    while True:
        print("""
1. Add Task
2. View All Tasks
3. View Pending Tasks
4. View Completed Tasks
5. View Tasks Due Soon
6. Mark Task as Completed
7. Edit Task
8. Delete Task
9. Show Task Graph
10. Exit
""")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_pending(tasks)
        elif choice == "4":
            view_completed(tasks)
        elif choice == "5":
            view_due_soon(tasks)
        elif choice == "6":
            complete_task(tasks)
        elif choice == "7":
            edit_task(tasks)
        elif choice == "8":
            delete_task(tasks)
        elif choice == "9":
            show_graph(tasks)
        elif choice == "10":
            save_tasks(tasks)
            print("Tasks saved")
            break
        else:
            print("Invalid choice.")

menu()
