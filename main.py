from storage import loadTasks, saveTasks
from datetime import datetime

tasks_list = loadTasks()

def next_id(tasks):
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1

def make_task(title, tasks):
    return {
        "id": next_id(tasks),
        "title": title.strip(),
        "done": False,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }

def addTask(title):
    title = title.strip()
    if not title:
        return False, "Task title cannot be empty."

    task = make_task(title, tasks_list)
    tasks_list.append(task)
    saveTasks(tasks_list)
    return True, "Task added."

def showTasks():
    if not tasks_list:
        return "You don't have any tasks."

    output = "\nTasks:\n"
    for i, task in enumerate(tasks_list, start=1):
        box = "[x]" if task["done"] else "[ ]"
        output += f"{i}. {box} {task['title']}\n"
    return output

def ask_task_number():
    if not tasks_list:
        return None

    raw = input(f"Enter task number (1-{len(tasks_list)}): ").strip()
    if not raw.isdigit():
        return None

    num = int(raw)
    if num < 1 or num > len(tasks_list):
        return None

    return num

def toggle_done(task_number):
    idx = task_number - 1
    tasks_list[idx]["done"] = not tasks_list[idx]["done"]
    saveTasks(tasks_list)

    state = "completed" if tasks_list[idx]["done"] else "not completed"
    return True, f"Task marked as {state}."

def edit_title(task_number, new_title):
    new_title = new_title.strip()
    if not new_title:
        return False, "Title cannot be empty."

    idx = task_number - 1
    tasks_list[idx]["title"] = new_title
    saveTasks(tasks_list)
    return True, "Task updated."

def confirm(prompt):
    ans = input(prompt + " (y/n): ").strip().lower()
    return ans == "y"

def delete_task(task_number):
    idx = task_number - 1
    title = tasks_list[idx]["title"]

    if not confirm(f'Delete "{title}"?'):
        return False, "Delete cancelled."

    tasks_list.pop(idx)
    saveTasks(tasks_list)
    return True, "Task deleted."

def menu():
    while True:
        print("\n--- STUDY TRACKER ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Toggle done/undone")
        print("4. Edit task title")
        print("5. Delete task")
        print("6. Exit")

        choice = input("Please select an option: ").strip()

        if choice == "1":
            title = input("Task title: ")
            _, message = addTask(title)
            print(message)

        elif choice == "2":
            print(showTasks())

        elif choice == "3":
            if not tasks_list:
                print("You don't have any tasks.")
                continue
            print(showTasks())
            num = ask_task_number()
            if num is None:
                print("Invalid task number.")
                continue
            _, msg = toggle_done(num)
            print(msg)

        elif choice == "4":
            if not tasks_list:
                print("You don't have any tasks.")
                continue
            print(showTasks())
            num = ask_task_number()
            if num is None:
                print("Invalid task number.")
                continue
            new_title = input("New title: ")
            _, msg = edit_title(num, new_title)
            print(msg)

        elif choice == "5":
            if not tasks_list:
                print("You don't have any tasks.")
                continue
            print(showTasks())
            num = ask_task_number()
            if num is None:
                print("Invalid task number.")
                continue
            _, msg = delete_task(num)
            print(msg)

        elif choice == "6":
            print("Exiting from Study Tracker...")
            break

        else:
            print("Invalid choice! Your choice should be 1-6.")

if __name__ == "__main__":
    menu()