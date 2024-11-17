def add_task(tasks, task):
    tasks.append(task)
    print(f"Added task: '{task}'")

def remove_task(tasks, task):
    if task in tasks:
        tasks.remove(task)
        print(f"Removed task: '{task}'")
    else:
        print(f"Task '{task}' not found in the to-do list.")

def display_tasks(tasks):
    if tasks:
        print("Current to-do list:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("The to-do list is empty.")

if __name__ == "__main__":
    to_do_list = []

    add_task(to_do_list, "Take dogs")
    add_task(to_do_list, "Eat samosa")
    display_tasks(to_do_list)

    remove_task(to_do_list, "Eat chole")
    display_tasks(to_do_list)

    remove_task(to_do_list, "Sleep")
    display_tasks(to_do_list)