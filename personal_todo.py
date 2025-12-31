# Personal To-Do List Application
import json
from datetime import datetime

FILE_NAME = "tasks.json"

#Task class 
class Task:
    def __init__(self, title, description, category, due_date="", completed=False, created_at=None):
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.completed = completed
        if created_at: 
            self.created_at = created_at
        else:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    def mark_completed(self):
        self.completed = True

#Load tasks from file 
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            tasks = []
            for task in data:
                tasks.append(Task(
                    title=task.get("title", ""),
                    description=task.get("description", ""),
                    category=task.get("category", ""),
                    due_date=task.get("due_date", ""),
                    completed=task.get("completed", False),
                    created_at=task.get("created_at", None)
                ))
            return tasks
    except FileNotFoundError:
        return []

#Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump([task.__dict__ for task in tasks], file, indent=4)

#Add new task 
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category (Work, Personal, Urgent): ")
    due_date = input("Enter due date (YYYY-MM-DD) or leave empty: ")
    task = Task(title, description, category, due_date)
    tasks.append(task)
    print("Task added successfully!")

#View all tasks 
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\n--- All Tasks ---")
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task.completed else "Pending"
        print(f"{i}. {task.title} | {task.description} | Category: {task.category} | Due: {task.due_date} | Status: {status}")

#Mark task completed
def complete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark completed: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num].mark_completed()
            print("Task marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a number!")

#Edit a task
def edit_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to edit: ")) - 1
        if 0 <= num < len(tasks):
            task = tasks[num]
            task.title = input("Enter new title: ")
            task.description = input("Enter new description: ")
            task.category = input("Enter new category: ")
            task.due_date = input("Enter new due date (YYYY-MM-DD): ")
            print("Task updated!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a number!")

#Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            removed_task = tasks.pop(num)
            print(f"Task '{removed_task.title}' deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a number!")

#Main menu 
def menu():
    tasks = load_tasks()
    while True:
        print("""
1. Add Task
2. View All Tasks
3. Mark Task Completed
4. Edit Task
5. Delete Task
6. Exit
""")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Tasks saved")
            break
        else:
            print("Invalid choice. Try again!")

#Run the program 
menu()
