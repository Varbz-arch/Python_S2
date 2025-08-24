class ToDoList:
    def __init__(self):
        self.tasks = []    #tasks is an instance variable
    def add_task(self):
        while True:
            task_name = input("\nEnter the task and type 'stop' if you are done: ")
            if task_name.lower() == "stop":
                break
            self.tasks.append({"task": task_name, "completed": False})
            print(f"Task '{task_name}' added successfully!")
    def display_tasks(self):
        if not self.tasks:
            print("\nNo tasks available!")
        else:
            print("\nYour To-Do List:\n")
            for index, task in enumerate(self.tasks, start=1):
                status = "Done" if task["completed"] else "Pending"
                print(f"{index}. {task['task']} [{status}]")
    def mark_task_complete(self):
        self.display_tasks()
        if not self.tasks:
            return
        try:
            task_no = int(input("\nEnter task number to mark as complete: ")) - 1
            if 0 <= task_no < len(self.tasks):
                self.tasks[task_no]["completed"] = True
                print(f"Task '{self.tasks[task_no]['task']}' marked as complete!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    def delete_task(self):
        self.display_tasks()
        if not self.tasks:
            return
        try:
            task_no = int(input("\nEnter task number to delete: ")) - 1
            if 0 <= task_no < len(self.tasks):
                deleted = self.tasks.pop(task_no)
                print(f"Task '{deleted['task']}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
def main():
    todo_list = ToDoList()
    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            todo_list.add_task()
        elif choice == "2":
            todo_list.display_tasks()
        elif choice == "3":
            todo_list.mark_task_complete()
        elif choice == "4":
            todo_list.delete_task()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
