# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to display the to-do list
def show_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to remove a task from the list
def remove_task():
    show_tasks()
    if tasks:
        try:
            task_number = int(input("Enter the number of the task to remove: "))
            if 1 <= task_number <= len(tasks):
                tasks.pop(task_number - 1)
            else:
                print("Invalid task number. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Show tasks")
    print("3. Remove a task")
    print("4. Quit")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Thank you.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
