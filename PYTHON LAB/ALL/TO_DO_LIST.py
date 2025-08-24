#TO DO LIST 
tasks = []

# def add_task():
#     task_name = input("\n Enter the task: ")
#     tasks.append({"task": task_name, "completed": False})  #by default it sets to false as assumed as not done yet
#     print(f" Task '{task_name}' added successfully!")

def add_task():
    while True:
        task_name = input("\nEnter the task  and type 'stop' if you are done: ")
        if task_name.lower() == "stop":
            break
        tasks.append({"task": task_name, "completed": False})
        print(f"Task '{task_name}' added successfully!")

def display_tasks():
    if not tasks:
        print("\n No tasks available!")
    else:
        print("\n Your To-Do List:\n")
        for index, task in enumerate(tasks, start=1):  #keeps track of the index without seperable counter
            status = " Done" if task["completed"] else "Pending"  #Condition for status
            print(f"{index}. {task['task']} [{status}]")  # 1. study [pending/ DONE]

def mark_task_complete():
    display_tasks()
    if not tasks:
        return
    try:
        task_no = int(input("\n Enter task number to mark as complete: ")) - 1  #for index, starts=0
        if 0 <= task_no < len(tasks):
            tasks[task_no]["completed"] = True  #change from false to true as it's task is completed
            print(f"Task '{tasks[task_no]['task']}' marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    display_tasks()
    if not tasks:
        return
    try:  #exception handling
        task_no = int(input("\n Enter task number to delete: ")) - 1
        if 0 <= task_no < len(tasks):
            deleted = tasks.pop(task_no)  #delete the task by index 
            print(f"Task '{deleted['task']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:  
        print("Please enter a valid number.")

def main():
    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":  #ensures that the script runs only when executed directly. 
    main()
