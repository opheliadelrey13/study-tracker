from storage import loadTasks,saveTasks

task_list = loadTasks()

def addTask(title):
    title = title.strip()
    if not title:
        return False, "Task title is required."
    task_list.append(title)
    saveTasks(task_list)
    return True, "Task added successfully."

def showTasks():
    if not task_list:
        return "You don't have any tasks."

    output = "\nTasks:\n"
    for i, task in enumerate(task_list, start=1):
        output += f"{i}. {task}\n"
    return output


def deleteTask(task_number):
    if not task_list:
        return False, "You don't have any tasks."
    if not str(task_number).isdigit():
        return False, "Please enter a valid task number."

    task_number = int(task_number)

    if task_number < 1 or task_number > len(task_list):
        return False, "Task number doesn't exist."

    removedTask = task_list.pop(task_number - 1)
    saveTasks(task_list)
    return True, f"Task {removedTask} deleted successfully."



def menu():
    while True:
        print("\n--- STUDY TRACKER ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Please select an option: ").strip()

        if choice == "1":
            title = input("Task title: ").strip()
            success, message = addTask(title)
            print(message)

        elif choice == "2":
            print(showTasks())

        elif choice == "3":
            print(showTasks())
            task_number = input("Enter the task number you want to delete: ").strip()
            success, message = deleteTask(task_number)
            print(message)
        elif choice == "4":
            print("Exiting from the Study Tracker...")
            break


        else:
            print("Invalid choice! Your choice should be 1, 2, or 3.")


if __name__ == "__main__":
    menu()