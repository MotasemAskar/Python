import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet. Enjoy your free time!")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, 1):
            status = "✓" if task["done"] else " "
            print(f"{idx}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("What do you want to add? ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print(f"Added: {title}")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Mark which task as done? (number): "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            print(f"Marked '{tasks[num-1]['title']}' as done.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nOptions: [1] Show [2] Add [3] Done [4] Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
            save_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye! Have a productive day.")
            break
        else:
            print("Please choose a valid option.")

if __name__ == "__main__":
    main()