tasks_list = []

def addTask():
    title = input("Task title: ")
    tasks_list.append(title)
    print("Task added.")

def getTasks():
    return tasks_list

def showTasks():
    currentTasks = getTasks()

    if not currentTasks:
        print("You don't have any tasks.")
    else:
        print("\nTasks:")
        for i, task in enumerate(currentTasks, start=1):
            print(f"{i}, {task}")

def menu():
    while True:
        print("\n---STUDY TRACKER---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3.Exit")

        choice = input("Please select an option: ")

        if choice == "1":
            addTask()
        elif choice == "2":
            showTasks()
        elif choice == "3":
            print("Exiting from Study Tracker...")
            break
        else:
            print("Invalid choice!\nYour choice shold be a number!")


if __name__ == "__main__":
    menu()