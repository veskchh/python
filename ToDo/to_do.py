from task_functions import add_task, remove_task, view_tasks, complete_task


tasks = []
while True:
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark Task Complete")
    print("5. Exit")
    choice = int(input("Choose an option: "))
    if not 0 < choice < 6:
        print("Choose a valid command.(1-5)")
        continue
    
    choice = int(choice)

    if choice == 1:
        task = input("What is your task?: ")
        add_task(tasks, task)
    elif choice == 2:
        view_tasks(tasks)
    elif choice == 3:
        view_tasks(tasks)
        task_num = int(input("What is the number of the task you want to remove?: "))
        remove_task(tasks, task_num)
    elif choice == 4:
        task_num = int(input("What is the number of the task you have completed?: "))
        complete_task(tasks, task_num)
    elif choice == 5:
        print("Exiting...")
        break
    



