tasks = []

while True:
    print("\n" + "-" * 25)
    print("1 - Add tasks")
    print("2 - Show tasks")
    print("3 - Remove a task")
    print("4 - Mark task as completed")
    print("5 - Exit")
    print("-" * 25)

    try:
        ch = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Enter a number.")
        continue

    # ADD TASKS
    if ch == 1:
        n = int(input("How many tasks you want to add: "))
        for i in range(n):
            task = input(f"Enter task {i+1}: ")
            tasks.append({"task": task, "done": False})

    # SHOW TASKS
    elif ch == 2:
        print("\n<--- Your To-Do List --->")
        if not tasks:
            print("No tasks found!")
        else:
            for i, t in enumerate(tasks, start=1):
                status = "✂️ DONE" if t["done"] else "❌ NOT DONE"
                print(f"{i}. {t['task']} [{status}]")

    # REMOVE TASK
    elif ch == 3:
        if not tasks:
            print("No tasks to remove!")
            continue
        
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t['task']}")
        
        try:
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Removed: {removed['task']}")
            else:
                print("Invalid number!")
        except ValueError:
            print("Enter a valid number!")

    # MARK AS COMPLETED
    elif ch == 4:
        if not tasks:
            print("No tasks to mark!")
            continue
        
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t['task']}")
        
        try:
            num = int(input("Enter task number to mark as done: "))
            if 1 <= num <= len(tasks):
                tasks[num - 1]["done"] = True
                print("Task marked as completed ✂️")
            else:
                print("Invalid number!")
        except ValueError:
            print("Enter a valid number!")

    # EXIT
    elif ch == 5:
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice! Try again.")
