def add_task(task_list, task):
    task_list.append(task)
    print("\nTask added!")
    
def complete_task(task_list, task_num):
    task_index = task_num - 1
    if 0 <= task_index < len(task_list):
        completed_task = task_list.pop(task_index)
        print(f"Task '{completed_task}' has been completed.")
    else:
        print("No such task exists.")

def remove_task(task_list, task_number):
    task_index = task_number - 1
    if 0 <= task_index < len(task_list):
        removed_task = task_list.pop(task_index)
        print(f"Task '{removed_task}' removed.")
    else:
        print("No such task exists.")

def view_tasks(task_list):
    if not task_list:
        print("No tasks available.")
    else:
        print("\nCurrent tasks are:")
        for index, task in enumerate(task_list):
            print(f"{index + 1}. {task}")