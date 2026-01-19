import os

tasks = []

if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as file:
        for line in file:
            task, status = line.strip().split("|")
            tasks.append([task, status == "done"])

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task, done in tasks:
            status = "done" if done else "not_done"
            file.write(f"{task}|{status}\n")

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append([task, False])
        save_tasks()
        print("Task added ✅")

    elif choice == "2":
        if not tasks:
            print("No tasks 📭")
        else:
            for i, (task, done) in enumerate(tasks, start=1):
                mark = "✔️" if done else "❌"
                print(f"{i}. {task} {mark}")

    elif choice == "3":
        num = int(input("Task number to mark done: "))
        tasks[num - 1][1] = True
        save_tasks()
        print("Task marked as done ✔️")

    elif choice == "4":
        num = int(input("Task number to delete: "))
        tasks.pop(num - 1)
        save_tasks()
        print("Task deleted 🗑️")

    elif choice == "5":
        print("Bye 👋")
        break

    else:
        print("Invalid choice ❗")
