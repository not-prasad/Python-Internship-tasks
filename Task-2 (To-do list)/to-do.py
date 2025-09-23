import os
TASKS_FILE = "tasks.txt"

def load_tasks():
    '''Return list of tasks (strings). If file missing, return empty list.'''
    if not os.path.exists(TASKS_FILE):
        return []
    tasks = []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line != "":
                tasks.append(line)
    return tasks




def save_tasks(tasks):
    """Save tasks (list of strings) to Tasks_file, one per line"""
    with open(TASKS_FILE, "w", encoding = "utf-8") as f:
        for t in tasks:
            f.write(f"{t}\n")



def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks. Enjoy your free time!\n")
        return
    print("\nYour tasks:")
    i = 1
    for t in tasks:
        print(f"{i}.{t}")
        i+=1
    print()


def add_task(tasks , task_text):
    task = task_text.strip()
    if task == "":
        print("Cannot add an empty task")
        return
    tasks.append(task)
    save_tasks(tasks)
    print(f'Added:{task}')



def remove_task(tasks, identifier):
    """
    Remove by number (1-based) if identifier is digit,
    otherwise try exact match, then try partial matches.
    """
    identifier = identifier.strip()
    if identifier == "":
        print("No identifier provided.")
        return

    # Remove by index
    if identifier.isdigit():
        idx = int(identifier) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            save_tasks(tasks)
            print(f'Removed: "{removed}"')
        else:
            print("Invalid task number.")
        return

    # Exact text match
    found_exact = False
    for t in tasks:
        if t == identifier:
            tasks.remove(t)
            save_tasks(tasks)
            print(f'Removed: "{t}"')
            found_exact = True
            break
    if found_exact:
        return

    # Partial case-insensitive matches
    matches = []
    for t in tasks:
        if identifier.lower() in t.lower():
            matches.append(t)

    if len(matches) == 0:
        print("No matching task found.")
    elif len(matches) == 1:
        tasks.remove(matches[0])
        save_tasks(tasks)
        print(f'Removed: "{matches[0]}"')
    else:
        print("Multiple matches found:")
        for i, t in enumerate(matches, 1):
            print(f"{i}. {t}")
        print("Please remove by number (view the full list and use the index).")



def clear_all(tasks):
    confirm = input("Are you sure you want to delete ALL tasks? (y/N): ").strip().lower()
    if confirm == "y":
        tasks.clear()
        save_tasks(tasks)
        print("All tasks cleared.")
    else:
        print("Cancelled.")                

def main():
    tasks = load_tasks()
    menu = """
Choose an option:
A - Add task
R - Remove task
V - View tasks
C - Clear all tasks
Q - Quit
    Enter choice: """
    while True:
        choice = input(menu).strip().lower()
        if choice == "a":
            task = input("Enter the task to add: ")
            add_task(tasks, task)
        elif choice == "r":
            view_tasks(tasks)
            identifier = input("Enter task number or text to remove: ")
            remove_task(tasks , identifier)
        elif choice == "v":
            view_tasks(tasks)
        elif choice == "c":
            clear_all(tasks)
        elif choice == "q":
            print("Saving and exiting. Bye!")
            break
        else:
            print("Unknown option. Try A,R,V,C or Q.")

if __name__ == "__main__":
    main()