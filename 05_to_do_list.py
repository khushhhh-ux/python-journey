tasks = []
while True:
    try:
        print('''
        ====================
        =====TO DO LIST=====
        ====================''')

        print("1. Add task")
        print("2. View task")
        print("3. remove task")
        print("4. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:

            while True:
                task = input("Enter task: ")
                print("Task added!")

                tasks.append(task)
                while True:
                    off = input("Do you want to add more tasks(y/n):  ").lower()
                    
                    if off == "n":
                        break

                    elif off != "y":
                        print("Invalid option!")

                    elif off == "y":
                        break

                if off == "n":
                    break

        elif choice == 2:
            if not tasks:
                print("No tasks available")

            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

            input("\nPress Enter to return to the main menu...")

        elif choice == 3:
            if not tasks:
                print("No tasks available!")
                print("\nPress Enter to return to the main menu...")
                continue

            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

            while True:
                remove = int(input("Do you want to remove a task: "))
                if 1 <= remove <= len(tasks):
                    tasks.pop(remove - 1)
                    print("Task Removed!")
                    print("\nPress Enter to return to the main menu...")
                    break

                else:
                    print("Invalid task number!")

        elif choice == 4:
            break

        else:
            print("Invalid choice!")
    except ValueError:
        print("Choose a valid choice")
    


