import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read task file.")
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    title = input("Enter task title: ").strip()
    priority = input("Enter priority (High/Medium/Low): ").strip().title()

    if not title:
        print("Task title cannot be empty!")
        return

    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority!")
        return

    task = {
        "id": max((t["id"] for t in tasks), default=0) + 1,
        "title": title,
        "priority": priority,
        "status": "Pending"
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")


def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- All Tasks ---")

    for task in tasks:
        print(
            f'ID: {task["id"]} | '
            f'Title: {task["title"]} | '
            f'Priority: {task["priority"]} | '
            f'Status: {task["status"]}'
        )


def complete_task(tasks):
    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Enter a valid ID!")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            save_tasks(tasks)
            print("Task completed!")
            return

    print("Task not found!")


def show_pending(tasks):
    pending = [task for task in tasks if task["status"] == "Pending"]

    if not pending:
        print("No pending tasks.")
        return

    print("\n--- Pending Tasks ---")

    for task in pending:
        print(f'{task["id"]}. {task["title"]} ({task["priority"]})')


def delete_task(tasks):
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Enter a valid ID!")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted!")
            return

    print("Task not found!")


tasks = load_tasks()

while True:
    print("\n===== PERSONAL TASK MANAGER =====")
    print("1. Add Task")
    print("2. Show All Tasks")
    print("3. Complete Task")
    print("4. Show Pending Tasks")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        show_tasks(tasks)

    elif choice == "3":
        complete_task(tasks)

    elif choice == "4":
        show_pending(tasks)

    elif choice == "5":
        delete_task(tasks)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
